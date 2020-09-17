import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from email_list import emails

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Nigga Blackson'
email['to'] = emails
email['subject'] = 'You won 1,000,000 dollars!'


email.set_content(html.substitute(name= 'Nigga'),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('neggerlovesuckdick@gmail.com', 'Nigga1999.')
	smtp.send_message(email)
	print('All done')