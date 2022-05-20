from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

sender = "user@example.com"
receivers = [
    "user@example.com",
    "user@example.com",
    "user@example.com"
]

title = ""
body = ""

# Settings preset for Protonmail Bridge
password = "from_bridge"
smtpserver = "127.0.0.1"
port = 1025
ssl = ssl._create_unverified_context()

message = MIMEMultipart()
message['From'] = sender
message['Subject'] = title
message.attach(MIMEText(body))

with smtplib.SMTP(smtpserver, port) as server:
    server.starttls(context=ssl)
    server.login(sender, password)
    try:
        for receiver in receivers:
            message['To'] = receiver
            server.sendmail(sender, receiver, message.as_string())
            print(message, "\nSuccessfully sent message to ", receiver, " via SMTP.")
    except Exception as e:
        print(e)
    finally:
        server.quit()