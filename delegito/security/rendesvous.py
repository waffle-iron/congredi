# -*- coding: utf-8 -*-
#https://cryptography.io/en/latest/fernet/
import os, sys, datetime, logging, time
from stem.control import Controller
from stem.util import term
from stem import process
#http://stackoverflow.com/questions/35437668/realtime-progress-tracking-of-celery-tasks/35438284#35438284
# https://gist.github.com/tmshv/9c0712b858ab1bbed976
TOR_CONTROLLER_PASS='my_password'
SOCKS_PORT = 9050
offered_keypath = os.path.expanduser('~/.komento/offered_rendesvous')
def print_bootstrap_lines(line):
	if "Bootstrapped " in line: print(term.format(line, term.Color.BLUE))
def start_tor():
	tor_process = process.launch_tor_with_config(
	config = {
	'SocksPort': str(SOCKS_PORT),
	'ControlPort': str(9051),
	'ExitNodes': '{ru}',
	},
	init_msg_handler = print_bootstrap_lines,
	)
	return tor_process
def stop_tor(tor_process):
	tor_process.kill()  # stops tor
def start_controller():
	logging.debug("Connect controller")
	timeout = 0
	while timeout < 60:
		try:
			controller = Controller.from_port(port=9051)
			controller.authenticate()
			return controller
		except:
			time.sleep(1)
			timeout += 1
	logging.critical("Could not connect to Tor controller")
	sys.exit(1)
def swap_controller(controller):
	controller.signal(Signal.NEWNYM)
	time.sleep(controller.get_newnym_wait())
def stop_controller(controller):
	controller.authenticate()

def write_conf(rendes):
	logging.debug("Writing rendesvous private key")
	with open(offered_keypath,'w+') as key:
		key.write('{}:{}'.format( rendes.private_key_type, rendes.private_key))

def offer_rendesvous(controller):
	logging.info("Begin rendesvous")
	#controller.get_hidden_service_descriptor('3g2upl4pq6kufc4m')
	#for introduction_point in desc.introduction_points():
	#	print('  %s:%s => %s' % (introduction_point.address, introduction_point.port, introduction_point.identifier))
	#	print("found relay %s (%s)" % (desc.nickname, desc.fingerprint))
	# new identity
	if not os.path.exists(offered_keypath):
		logging.debug("Creating new rendesvous")
		response = controller.create_ephemeral_hidden_service({80:5000}, await_publication = True)
		write_conf(response)
	else:
		logging.debug("Loading old rendesvous")
		try:
			with open(offered_keypath,'r') as key:
				ktype, keyc = key.read().split(':', 1)
				response = controller.create_ephemeral_hidden_service({80: 5000}, key_type = ktype, key_content = keyc, await_publication = True)
		except:
			response = controller.create_ephemeral_hidden_service({80:5000}, await_publication = True)
			logging.warming("Old rendesvous corrupted.")
			write_conf(response)
	offered_rendesvous = response.service_id
	# result.hostname
	return offered_rendesvous
