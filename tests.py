#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from nose2.tools import with_setup, raises
from flask import json
from structs.keyvalues import make_active, remove_active
from structs.crypto import Crypto, Learner

from delegito import app

fl = app
fl.config['TESTING'] = True
app = fl.test_client()

class TestTokens(object):
	def test_tokens(self):
		print('Testing Tokens')
		token = make_active('test','ab')
		token = make_active('bets','cb',True)
		remove_active(token)
	@classmethod
	def setup_class(self):
		print('setup')
	@classmethod
	def teardown_class(self):
		print('teardown')

class TestCrypto(object):	
	def test_crypto(self):
		print('Testing Crypto')
		co = Crypto()
class TestLearner(object):	
	def test_learner(self):
		print('Testing Learner')
		le = Learner()
class TestMongo(object):
	def test_mongo(self):
		print('Mongo tests')
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
			print('WIP: need to pass json into request.form?!?!')
#https://github.com/pallets/flask/blob/7c271401b284e6fcc2040fffe317342e2a17a902/tests/test_helpers.py
#https://github.com/pallets/flask/blob/c9b29f4072b66be4c751af060d64ea749c6991c1/tests/test_templating.py
#https://github.com/pallets/flask/blob/e048aa4e19d689104733783a19560a6a485a473c/tests/test_basic.py
