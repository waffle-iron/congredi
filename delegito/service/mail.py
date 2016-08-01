#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from delegito.config import password
def mail(address, subject, plain, html):
	print('Sending an Email.')
	return
	msg = MIMEMultipart('alternative')
	msg['From'] = "server@delegito.io"
	msg['To'] = address
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject
	msg.attach( MIMEText(plain, 'plain') )
	msg.attach( MIMEText(html, 'html') )
	server = smtplib.SMTP('delegito.io')
	server.login("server@delegito.io", str(password))
	server.sendmail("server@delegito.io", address, msg.as_string())
	server.quit()
dirname, filename = os.path.split(os.path.abspath(__file__))
def retr(name):
	with open(dirname + '/templates/' + name, 'r') as file:
		return file.read()
templates = {
	'register':retr('register.html')
	}
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
