import smtplib
import ssl
import sys

def log(em, p, HOST="smtp.gmail.com", PORT=465):
    smtp = smtplib.SMTP_SSL(HOST, PORT, context=ssl.create_default_context())
    try:
        smtp.ehlo()
        smtp.login(em, p)
    except Exception as e:
        print("Something going wrong")
        sys.exit(1)
    return smtp

def send(smtp, user_em, p, req_em, subject, mes, HOST="smtp.gmail.com", PORT=465):
    msg = f"Subject: {subject}\n\n{mes}"
    smtp.sendmail(user_em, req_em, msg, )
    print("Success!")

def end_work(smtp): smtp.quit()
