# LIBS
from smtp import *
from smtplib import *
from CONFIG import password

# LOGIN
usr_mail = input('User email: ')
smtp_api = log(usr_mail, password)

# GET MSG
req_mail = input('Recipient email: ')
sub = input('Your subject: ')
mes = input('Your message: ')

# SEND 
send(smtp_api, usr_mail, password, req_mail, sub, mes)

# END
end_work(smtp_api)
