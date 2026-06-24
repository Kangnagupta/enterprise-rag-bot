import os
from fpdf import FPDF

def create_pdf(filename, title, content):
    """Creates a simple PDF file with a title and text content."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt=title, ln=1, align='C')
    pdf.ln(10) # Add a line break
    
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, txt=content)
    pdf.output(filename)
    print(f"Created: {filename}")

def main():
    # Ensure the data directory exists
    os.makedirs("./data", exist_ok=True)
    
    # Mock IT Helpdesk Policies
    policies = {
        "VPN_Access_Policy.pdf": (
            "VPN Access Policy\n\n"
            "To connect to the corporate VPN, employees must use the Cisco AnyConnect client. "
            "Multi-Factor Authentication (MFA) via the Okta app is strictly required. "
            "If your VPN drops frequently, please ensure your home router firmware is updated "
            "and switch to the TCP protocol in the Cisco client settings. "
            "VPN access is automatically revoked after 90 days of inactivity."
        ),
        "Password_Reset_Guidelines.pdf": (
            "Password Reset Guidelines\n\n"
            "Corporate passwords must be at least 14 characters long and include a mix of uppercase, "
            "lowercase, numbers, and symbols. Passwords expire every 60 days. "
            "To reset your password, visit auth.company.internal. Never share your password "
            "with the IT helpdesk. We will never ask for it."
        ),
        "Hardware_Request_Process.pdf": (
            "Hardware Replacement Process\n\n"
            "Employees are eligible for a laptop refresh every 3 years. To request a new laptop, "
            "submit a Jira ticket under the 'Hardware' project. Manager approval is required for "
            "all MacBook Pro requests. Broken peripherals (mice, keyboards) can be replaced "
            "by visiting the IT kiosk on the 3rd floor without prior approval."
        )
    }

    print("Generating mock enterprise documents...")
    for filename, content in policies.items():
        create_pdf(f"./data/{filename}", filename.replace('.pdf', ''), content)
    
    print("\nSuccess! Sample PDFs are ready in the './data' folder.")

if __name__ == "__main__":
    main()