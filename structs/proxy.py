# https://gist.github.com/tmshv/9c0712b858ab1bbed976
TOR_CONTROLLER_PASS='password'
SOCKS_PORT = 9050
offered_keypath = os.path.expanduser('~/.komento/offered_rendesvous')
def start_tor():
	tor_process = stem.process.launch_tor_with_config(
	config = {
	'SocksPort': str(SOCKS_PORT),
	'ExitNodes': '{ru}',
	},
	init_msg_handler = print_bootstrap_lines,
	)
	return tor_process
def stop_tor():
	tor_process.kill()  # stops tor
def start_controller():
	logging.debug("Connect controller")
	controller = Controller.from_port(port=9051)
	if not controller:
		logging.critical("Could not connect to Tor controller")
		sys.exit(1)
	controller.authenticate()
	return controller
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
def proxy_ask(url):
	# socks -> urllib2 -> get
	# socks
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT)#, True)
	socket.socket = socks.socksocket
	# urllib2
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
	urllib2.urlopen('http://www.google.fr').read()
	proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8118'})
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	print(urllib2.urlopen(ipcheck_url).read())
	# requesocks
	session = requesocks.session()
	session.proxies = {'http':  'socks5://127.0.0.1:9050',
	                   'https': 'socks5://127.0.0.1:9050'}
	print session.get("http://httpbin.org/ip").text
	try:
		requests.get('http://{}.onion'.format(friend_rendesvous))
	except requests.HTTPError:
		logging.error("Failed: {}".format(friend_rendesvous))
	# pycurl
	output = StringIO.StringIO()
	output = io.BytesIO()
	query = pycurl.Curl()
	query.setopt(pycurl.URL, url)
	query.setopt(pycurl.PROXY, 'localhost')
	query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
	query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
	query.setopt(pycurl.CONNECTTIMEOUT, CONNECTION_TIMEOUT)#unnessessary?
	query.setopt(pycurl.WRITEFUNCTION, output.write)
	try:
		query.perform()
		return output.getvalue()
	except pycurl.error as exc:
		raise ValueError("Unable to reach %s (%s)" % (url, exc))
