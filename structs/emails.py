from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders
def mail(address,subject,message):
	print('Sending an Email.')
	return
	html = formatHtml()
	msg = MIMEMultipart('alternative')
	msg['From'] = "server@delegito.io"
	msg['To'] = address
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject
	msg.attach( MIMEText(message, 'plain') )
	msg.attach( MIMEText(html, 'html') )
	server = smtplib.SMTP('delegito.io')
	server.login("server@delegito.io",str(password))
	server.sendmail("server@delegito.io", address, msg.as_string())
	server.quit()
"""
https://github.com/mailchimp/email-blueprints
https://github.com/leemunroe/responsive-html-email-template
https://github.com/mailgun/transactional-email-templates
https://github.com/g13nn/Email-Framework
https://github.com/charlesmudy/responsive-html-email-template
https://github.com/zurb/foundation-emails-template
https://github.com/zurb/foundation-emails
https://github.com/frascoweb/frasco-emails
"""