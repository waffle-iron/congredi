#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, json, Response,render_template, session, request, redirect, url_for, escape
import logging, traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders
#from delegito import *

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


"""
/api/
	/auth/          [POST|DELETE] - db
	/token/         [GET|DELETE] - JWT
	/bearing/       [GET|DELETE] - JWT (longer time)
	/search/:type
		?offset=0?limit=0 {term:"",author:""} - search
	/storage/:type
		/(new|:id)/ [POST|GET|UPDATE|DELETE]
"""

def userdata(request,e=True):
	j = request.get_json()
	print j
	# required fields (could for loop this)
	# validate & escape fields for db
	try: username = j['username']
	except: raise Exception('Username Required')
	try: password = j['password']
	except: raise Exception('Password Required')
	if e:
		try: email = j['email']
		except: raise Exception('Email Required')
		return username, password, email
	return username, password

app = Flask('Delegito')
@app.route('/api/auth/',methods=['POST','DELETE'])
def db_authorize():
	ac = request.method
	if ac == 'POST':
		u, p, e = userdata(request)
		mid = mongo_start(u, p, e)
		if 'error' not in mid.keys():
			token = mongo_token(u,p)
			response = make_active(token,secret)
		else: response = mid
		return jsonify(response)
	elif ac == 'DELETE':
		u, p = userdata(request,e=False)
		mid = check_active(request,secret)
		if 'error' not in mid.keys():
			mid = mongo_stop(u,p)
			if 'error' not in mid.keys():
				response = remove_active(mid)
			else: response = mid
		else: response = mid
		return jsonify(response)
@app.route('/api/token/',methods=['GET','DELETE'])
def session_control():
	ac = request.method
	if ac == 'GET':
		username, password = userdata(request,e=False)
		mid = mongo_token(username,password)
		if 'error' not in mid.keys():
			response = make_active(username,secret)
		else: response = mid
	elif ac == 'DELETE':
		mid = check_active(request,secret)
		if 'error' not in mid.keys():
			response = remove_active(mid)
		else: response = mid
	return jsonify(response)
# like... oauth2?
@app.route('/api/bearing/',methods=['GET'])
def long_bearer():
	# records.find(query).skip(offset).limit(limit)
	username, password = userdata(request,e=False)
	mid = check_active(request,secret)
	if 'error' not in mid.keys():
		make_active(username,secret,bearing=True)
	else:
		result = mid
	return jsonify(result)
@app.route('/api/search/<recordType>',methods=['GET'])
def search_mongo(recordType):
	# records.find(query).skip(offset).limit(limit)
	mid = check_active(request,secret)
	if 'error' not in mid.keys():
		query = request.get_json()['query']
		if recordType == 'users':
			result = users.find_one({recordType:query})
		elif recordType == 'records':
			result = records.find_one({recordType:query})
		if result is None:
			result = {'info':'Nothing by that name...'}
	else:
		result = mid
	return jsonify(result)
@app.route('/api/storage/<recordType>/<uuid>',methods=['GET','POST','PUT','UPDATE'])
def executeIO(recordType,uuid):
	mid = check_active(request,secret)
	if 'error' not in mid.keys():
		ac = request.method
		if ac == 'GET':
			query = request.get_json()['query']
			if recordType == 'users':
				result = users.find_one({recordType:query})
			elif recordType == 'records':
				result = records.find_one({recordType:query})
		else:
			record = request.get_json()
			if ac == 'POST':
				if recordType == 'users':
					users.push_one(query)
				elif recordType == 'records':
					records.push_one(query)
				result = {'success':'successfully added'}
			else:
				if recordType == 'users':
					users.update_one(query)
				elif recordType == 'records':
					records.update_one(query)
				result = {'success':'successfully updated'}
		if result is None:
			result = {'info':'Nothing by that name...'}
	else: result = mid
	return jsonify(result)

@app.errorhandler(404)
def not_found(error):
	print('route: error')
	from flask import make_response
	return make_response(jsonify( { 'error': 'Notfound' } ), 404)

class browser():
	def __init__(self):
		self.peers = [{"pgpkey":["rendesvous"]}]
	def check_addr(self, peer):
		found = False
		for rend in peer:
			res = proxy_ask(rend + '/id')
			if res['pubkey'] != peer.keys()[1]:
				return rend
		return found
	def new_peer(self, addr):
		res = proxy_ask(addr + '/id')
		peer = {
			"pubkey":res['pubkey'],
			"rendesvous":res['rendesvous'],
			"onion":res['onion'],
			"torchat":res['torchat'],
			"bitcoin":res['bitcoin'],
			"other":res['other']
		}
	def pull_index(self, addr):
		res = proxy_ask(addr + '/summary')
		total_records = res['totals']['records']
		total_peers = res['totals']['peers']
		records = res['records'] #sha256id, sigrev
		peers = res['peers'] #pubkey, rendesvous
		return records, peers
	def query_addr(self, addr,key,value):
		res = proxy_ask('{}/search/{}/{}'.format(addr,key,value))
		count = res['count']
		results = res['results']#sha256id, sigrev, auth, sig
	def get_content(self, addr,sha256id):
		res = proxy_ask('{}/content/{}')
		rev = res['sigrev']
		auth = res['author']
		body = res['body']
		precients = res['precidents']
		fallacies = res['fallacies']
		date = res['date']
	def run(self):
		# get content from peers
		for friend in friends:
			done = 2
			while done > 0:
				done = 0
				for friend in db.friends:
					addr = check_addr(friend)
					records, peers = pull_index(addr)
					for content in records:
						if db_search(content['sha256id']).count() == 0:
							con = get_content(addr,content['sha256id'])
							done += 1
					for peer in peers:
						if db_search(content['pubkey']).count() == 0:
							p = new_peer(peer['rendesvous'])
							done += 1

logger = logging.getLogger('delegito')
logger.setLevel(logging.WARNING)
logging.debug('Loaded API')
if __name__ == '__main__':
	logging.getLogger('stem').setLevel(logging.WARNING)
	logging.getLogger('flask').setLevel(logging.INFO)
	logging.basicConfig(level=logging.DEBUG)
	logger = logging.getLogger(__name__)
	logging.info('Welcome to Komento')
	try:
		controller = start_controller()
		offered_rendesvous = offer_rendesvous(controller)
		logging.info("Access rendesvous on: http://%s.onion" % offered_rendesvous)
		app.run(host="0.0.0.0",port=5000,debug=True)
	except:
		logging.critical(traceback.format_exc())
	finally:
		logging.info("Komento - shutdown.")
		try:
			controller.from_port().remove_ephemeral_hidden_service(offered_rendesvous)
			controller.close()
			stop_tor()
			logging.debug("rendesvous deleted successfully")
		except:
			pass
#http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
#https://pypi.python.org/pypi/Flask-Zurb-Foundation/0.2.1
#https://pypi.python.org/pypi/premailer/
