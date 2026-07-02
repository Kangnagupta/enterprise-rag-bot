# 1. Use an official, lightweight Python image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Install system dependencies required for some AI libraries
RUN apt-get update && apt-get install -y build-essential

# 4. Copy the requirements file first (this caches dependencies to save time)
COPY requirements.txt .

# 5. Install the Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your project files (src code, database, mock data)
COPY . .

# 7. Set the command to run your bot when the container starts
CMD ["streamlit", "run", "bot.py", "--server.port=8501", "--server.address=0.0.0.0"]