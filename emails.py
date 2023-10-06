import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email server configuration
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "your_username"
smtp_password = "your_password"

# Create a message
subject = "Hello, World!"
from_email = "your_email@example.com"
to_email = "recipient@example.com"

msg = MIMEMultipart()
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = subject
body = "This is a test email sent from Python."
msg.attach(MIMEText(body, "plain"))

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Error: {str(e)}")
