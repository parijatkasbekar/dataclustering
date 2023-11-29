import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
 
# Email configuration
sender_email = os.getenv('SENDER_EMAIL')
receiver_email = os.getenv('RECEIVER_EMAIL')
password = os.getenv('EMAIL_PASSWORD')
build_status = os.getenv('BUILD_STATUS')
build_url = os.getenv('BUILD_URL')
 
 
 
def main():
    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "JENKINS BUILD STATUS"
 
    # Email body
    body = f"The last build has been {build_status}. Please check the {build_url}"
    msg.attach(MIMEText(body, 'plain'))
 
    # Initialize the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
 
    # Login to your Gmail account
    server.login(sender_email, password)
 
    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
 
    # Close the SMTP server
    server.quit()
 
 
 
if __name__ == '__main__':
    main()