import email, getpass, imaplib, os, sys
import passwords
detach_dir = '.'
user = passwords.g_u
pwd = passwords.g_p
sender_email = 'sukeshkumar.2016@vitstudent.ac.in'
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select('"[Gmail]/All Mail"')
resp, items = m.search(None, 'FROM', '"%s"' % sender_email)
items = items[0].split()
for emailid in items:
    resp, data = m.fetch(emailid, "(RFC822)")
    email_body = str(data[0][1])
    mail = email.message_from_string(email_body)
    if mail.get_content_maintype() != 'multipart':
        continue
    subject = ""
    if mail["subject"] is not None:
        subject = mail["subject"]
    print("["+mail["From"]+"] :" + subject)
    for part in mail.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        filename = part.get_filename()
        counter = 1
        if not filename:
            filename = 'part-%03d%s' % (counter, 'bin')
            counter += 1
        att_path = os.path.join(detach_dir, filename)
        if not os.path.isfile(att_path) :
            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()
