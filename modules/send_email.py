import smtplib

sender = "lishayko@gmail.com"
reciever = "trinadesiat@yandex.ru"
password = "oevdonybkasuftlt"
subject = "Python Email Test"
body = "Testing sending email with Python."

# header
message = f"""From: {sender}
To: {reciever}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in....")
    server.sendmail(sender, reciever, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError as e:
    print(e)
    print("Unable to login")
