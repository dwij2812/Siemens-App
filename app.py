import smtplib
import passwords
##Email Login id Password Will go here
gmail_user = passwords.gmail_user
gmail_password = passwords.g_p

sent_from = gmail_user
to = ['dwijhariket@gmail.com', 'sukeshkumar.2016@vitstudent.ac.in']
subject = 'Test Message via Python'
body = "This is an automated message sent by Siemens BT \n\n- Siemens"

email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    print('\nConnection Established.......\n')
    server.login(gmail_user, gmail_password)
    print('User Authenticated...........\n')
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email sent!')
except:
    print('Something went wrong...')
