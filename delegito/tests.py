#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import json
from database import make_active, remove_active
from api import app
fl = app
fl.config['TESTING'] = True
app = fl.test_client()
class TestTokens(object):
	def test_tokens(self):
		print('Testing Tokens')
		token = make_active('test','ab')
		token = make_active('bets','cb',True)
		remove_active(token)
	@classmethod #from nose2.tools import with_setup, raises
	def setup_class(self):
		print('setup')
	@classmethod
	def teardown_class(self):
		print('teardown')
class TestMongo(object):
	def test_mongo(self):
		print('https://github.com/vmalloc/mongomock')
#https://github.com/pallets/flask/blob/7c271401b284e6fcc2040fffe317342e2a17a902/tests/test_helpers.py
#https://github.com/pallets/flask/blob/c9b29f4072b66be4c751af060d64ea749c6991c1/tests/test_templating.py
#https://github.com/pallets/flask/blob/e048aa4e19d689104733783a19560a6a485a473c/tests/test_basic.py
class TestFlask(object):
	def test_auth(self):
		print('Testing Auth')
		try:
			aj = app.post('/api/auth/',
				headers={
					'Authorization':'abc'},
				data=json.dumps({
					'username': 'abc',
					'password': 'def',
					'email':'a@c'
				}))
			print(aj)
		except:
			print('WIP: need to pass json into request.form?!?! http://flask.pocoo.org/docs/0.11/testing/')
