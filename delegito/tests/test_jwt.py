#!/usr/bin/env python
# -*- coding: utf-8 -*-
from delegito import make_active, remove_active
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
