import smtplib
import email.utils
from email.mime.text import MIMEText


msg = MIMEText ('The contents are in the body')

msg['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))

msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))

msg['Subject'] = 'This is a message to test smtp python3'

server = smtplib.SMTP('localhost',1025)

# server.set_debuglevel(True) # show comm with the server

try:
	server.sendmail('identifierSender@server.com',
			['identifierRecv@server.com'],
			msg.as_string())
finally:
	server.quit()

