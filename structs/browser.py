#!/usr/bin/env python
from structs.dataset import *
from structs.proxy import *
#https://gist.github.com/abishur/2482046
#pygame? easygui? gtk? openmp graphics?
# build files in dir
#https://github.com/vmalloc/mongomock
dotfiles = mongols()
client = open_journal()
#dataset.local.connect()
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
def curse():
	try:
		ui = curses.initscr()
		ui.clear()
		curses.noecho()
		curses.cbreak()
		ui.keypad(1)
		ui.border(0)
		ui.addstr(12, 25, "Komento")
		ui.refresh()
		return ui
	except:
		traceback.print_exc()
def mainmenu(screen):
	#main view
	screen.addstr(2, 2, "Please enter a number...")
	screen.addstr(4, 4, "1 - Add a user")
	screen.addstr(5, 4, "2 - Restart Apache")
	screen.addstr(6, 4, "3 - Show disk space")
	screen.addstr(7, 4, "4 - Exit")
	screen.refresh()
	# Frame the interface area at fixed VT100 size
	#global screen
	#screen = ui.subwin(23, 79, 0, 0)
	#screen.box()
	#screen.hline(2, 1, curses.ACS_HLINE, 77)
	#screen.refresh()
	#file_menu = ("File","file_func()")
	#proxy_menu = ("Proxy Mode", "proxy_func()")
	#doit_menu = ("Do It!", "doit_func()")
	#help_menu = ("Help", "help_func()")
	#exit_menu = ("Exit", "EXIT")
	# Add the topbar menus to screen object
	#topbar_menu((file_menu, proxy_menu, doit_menu, help_menu, exit_menu))
	return screen.getch()
def fieldentry(screen, prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input
def file_func():
	pad = curses.newpad(100, 100)
	for y in range(0, 100):
		for x in range(0, 100):
			try:
				pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
			except curses.error:
				pass
		pad.refresh(0,0, 5,5, 20,75)
		begin_x = 20; begin_y = 7
		height = 5; width = 40
		win = curses.newwin(height, width, begin_y, begin_x)
		s = curses.newwin(5,10,2,1)
		s.box()
		s.addstr(1,2, "I", hotkey_attr)
		s.addstr(1,3, "nput", menu_attr)
		s.addstr(2,2, "O", hotkey_attr)
		s.addstr(2,3, "utput", menu_attr)
		s.addstr(3,2, "T", hotkey_attr)
		s.addstr(3,3, "ype", menu_attr)
		s.addstr(1,2, "", hotkey_attr)
		s.refresh()
		c = s.getch()
		if c in (ord('I'), ord('i'), curses.KEY_ENTER, 10):
			curses.echo()
			s.erase()
			screen.addstr(5,33, " "*43, curses.A_UNDERLINE)
			cfg_dict['source'] = screen.getstr(5,33)
			curses.noecho()
		else:
			curses.beep()
			s.erase()
		return CONTINUE

if __name__ == "__main__":
	ui = curse()
	try:
		print "UI success"
		x = 0
		while x != ord('4'):
			mainmenu(ui)
			if x == ord('1'):
				username = fieldentry(ui,"Enter the username")
				homedir = fieldentry(ui,"Enter the home directory, eg /home/nate")
				groups = fieldentry(ui,"Enter comma-separated groups, eg adm,dialout,cdrom")
				shell = fieldentry(ui,"Enter the shell, eg /bin/bash:")
				curses.endwin()
		print "exits"
		while topbar_key_handler():
			draw_dict()
		ui.getch()
		curses.nocbreak(); ui.keypad(0); curses.echo()
		curses.endwin()
		print("Info: Running network scan...")
		browser.run()
	except IOError, exc:
		print "Errors"
		print(exc)
	finally:
		print "Finally"
		curses.nocbreak(); ui.keypad(0); curses.echo()
		curses.endwin()
		# shutdown
		print("Info: Browser shutting down...")
		shutdown(client)
