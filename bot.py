import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import chromadb

# 1. Set up the Web Page
st.set_page_config(page_title="IT Helpdesk Bot", page_icon="🤖")
st.title("🤖 IT Helpdesk Bot")

# 2. Load the AI Brain (Cached so it only loads ONCE)
@st.cache_resource
def load_ai_brain():
    # Loading TinyLlama - a highly efficient, fast model perfect for our server
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    
    # Create the generator pipeline
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=250)
    return pipe

# 3. Load the Memory (Cached)
@st.cache_resource
def load_memory():
    # Pointing to the chroma_db folder we saw in your project!
    client = chromadb.PersistentClient(path="./chroma_db") 
    # Get your knowledge base (you can change "knowledge_base" to your actual collection name if it's different)
    collection = client.get_or_create_collection(name="knowledge_base")
    return collection

# Boot up the systems! (Shows a spinning wheel on the website while loading)
with st.spinner("Initializing AI Core and Memory... (This takes a moment on startup)"):
    llm = load_ai_brain()
    db = load_memory()

# 4. Create the Chat Memory for the webpage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. The Chat Logic
if user_input := st.chat_input("Ask a helpdesk question: "):
    # Show user message on screen
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # --- RAG LOGIC: Search Memory ---
    # We ask Chroma for the 2 most relevant chunks of data to the user's question
    results = db.query(query_texts=[user_input], n_results=2)
    
    # Safely extract the documents, or default to a fallback if memory is empty
    if results['documents'] and len(results['documents'][0]) > 0:
        context_str = " ".join(results['documents'][0])
    else:
        context_str = "No specific IT documentation found for this query."

    # --- RAG LOGIC: Format the Prompt ---
    # TinyLlama uses this specific format to know what context it has to work with
    prompt = f"<|system|>\nYou are a helpful IT Helpdesk assistant. Answer the user's question using ONLY this context: {context_str}</s>\n<|user|>\n{user_input}</s>\n<|assistant|>\n"
    
    # Generate and show bot message on screen
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            output = llm(prompt)
            # Slice off the prompt text so we only show the AI's actual answer
            response_text = output[0]['generated_text'].split("<|assistant|>\n")[-1]
            st.markdown(response_text)
            
    st.session_state.messages.append({"role": "assistant", "content": response_text})