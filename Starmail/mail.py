import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = 'mihanccnt@gmail.com'

with open('password', 'r') as file:
    password = file.read()

receiver = 'mihan.edirisinghe@gmail.com'
subject = 'test'
body = 'This is an email send from python'

message = MIMEMultipart()
message['from'] = sender
message['to'] = receiver
message['subject'] = subject
message.attach(MIMEText(body, 'plain'))

filename = 'picture.jpg'
attachement = open(filename, 'rb')

load = MIMEBase('application', 'octet-stream')
load.set_payload(attachement.read())

encoders.encode_base64(load)
load.add_header('Content-Disposition', f'attachment; filename = {filename}')
message.attach(load)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)

text = message.as_string()
server.sendmail(sender, receiver, text)

server.quit()