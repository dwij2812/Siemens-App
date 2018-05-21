from matplotlib import pyplot as plt
from matplotlib import style
import numpy
from numpy import genfromtxt
import smtplib
import csv
import passwords

k = genfromtxt('example2.csv',delimiter=',',names=True)
data=k['reading']
l= genfromtxt('example.csv',delimiter=',',names=True)
data2=l['reading']
data=data[~numpy.isnan(data)]
print(data)
listobj=data.tolist()
print(listobj)
plt.plot(data)
plt.plot(data2)
plt.title('Plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
crossed=0
item=0
strf=''
with open('example2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    for row in readCSV:
        date = row[1]
        dates.append(date)
print(dates)
for i in listobj:
    item+=1
    if i>40:
        print('Value Crossed')
        crossed+=1
        strf+=str(crossed)+'.'+'\t'+str(i)+'\t'+str(dates[item-1])+'\n'
    else:
        print('Value OK')
print('\n The Value Has Been crossed ',crossed,' Out of ',item,' no of times')
strf=strf[:-1]
##This is the email logic
gmail_user = passwords.g_u
gmail_password = passwords.g_p

sent_from = gmail_user
to = ['dwijhariket@gmail.com', 'sukeshkumar.2016@vitstudent.ac.in']
subject = 'ALERT!! Meter Reading crossing Threshold'
body = "This is an automated message sent by Siemens Advanced Service Center, India \n The Value has crossed the threshold at reading number:\n\n"
body+=strf
body+='\n\n-Siemens India'
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
    print('\n\n This is the body of the email')
    print(body)
    #server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email sent!')
except:
    print('Something went wrong...')
