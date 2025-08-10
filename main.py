# LIBS
from CONFIG import access_password, mail_password
from smtp import *
from smtplib import *
from imap import *
from sys import exit

# LOGIN
usr_mail = input('User email: ')
p        = input('Password: ')
if (p != mail_password):
    print("Access denied!")
    exit(1)
smtp_api = log(usr_mail, access_password)
print("Access!")

while (1):
    # What to do
    prompt = input('Read/Print/Exit(r/p/e): ')

    # Do
    if (prompt == 'r'):
        N = int(input("How many to see: "))
        read(usr_mail, access_password, N)
    elif (prompt == 'p'):
        # GET MSG
        req_mail = input('Recipient email: ')
        sub = input('Your subject: ')
        mes = input('Your message: ')

        # SEND
        send(smtp_api, usr_mail, access_password, req_mail, sub, mes)
    elif (prompt == 'e'):
        # END
        end_work(smtp_api)
        break
    else:
        print("Unknown command x(")
