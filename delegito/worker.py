#!/usr/bin/env python
# -*- coding: utf-8 -*-
from celery import Celery
import logging, traceback
from service.mail import mail, templates

worker = Celery('delegito', backend='rpc://', broker='redis:my_password//db', track_started=True)
@worker.task(name='emailRegistration')
def emailRegistration(username):
	user = db.find_one(username)
	name = user.name; key = user.key; addr = user.email
	message = templates.register.replace('SU', name).replace('SF', key)
	mail(addr,
		 'Welcome to Congredi {}'.format(name),
		 message)
#http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
#https://pypi.python.org/pypi/Flask-Zurb-Foundation/0.2.1
if __name__ == '__main__':
	options = [
		'worker',
        '--broker=redis:my_password//db',
        'loglevel=INFO',
    ]
	worker.worker_main(options)#.run(**options)