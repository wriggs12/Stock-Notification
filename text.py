import smtplib
from email.message import EmailMessage
from datetime import date

def sendMessage(content, user, key, to):
    msg = EmailMessage()
    msg.set_content(content)
    msg['subject'] = str(date.today())
    msg['to'] = to

    msg['from'] = "John Bot"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, key)
    server.send_message(msg)

    server.quit()

def main():
    return

if __name__ == "__main__":
    main()