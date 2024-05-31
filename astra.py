import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Coded by Astra

# smtp-settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = "mail"
smtp_password = "password"

# easy-type
subject = 'Enter Subject'
message_text = "Enter Message (Optional)"

# html-type
html_message = """
Enter html here. (Optional)
"""


with open('astra-mail.txt', 'r') as file:
    to_emails = file.read().splitlines()


for to_email in to_emails:
    msg = MIMEMultipart('alternative')
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(html_message, 'html'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())
        server.quit()
        print(f'E-mail successfully {to_email} sent to address. | coded by astra')
    except Exception as e:
        print(f'E-mail sending error ({to_email}): {str(e)} | coded by astra')
        
    time.sleep(45)