#!/usr/bin/env python
from dataset import *
from proxy import *
logging.getLogger('stem').setLevel(logging.WARNING)
logging.getLogger('flask').setLevel(logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
crier = Flask(__name__)
@crier.errorhandler(404)
def page_not_found(e):
	return 'Sorry, Nothing at this URL.', 404
@crier.route('/id')
def id():
	return jsonify(server)
@crier.route('/summary')
def summary():
	return jsonify(dataset_idx())
@crier.route('/search/<key>/<value>')
def search(key,value):
	res = db.find({key:value})
@crier.route('/content/<sha256>')
def serve(sha256):
	res = db.find({"_id":sha256})#global heuristic instead of local `_id`?
	return jsonify(res)
if __name__ == "__main__":
	logging.info('Welcome to Komento')
	dotfiles = mongols()
	db = open_journal()
	server = search_journal({'server'})
	try:
		controller = start_controller()
		offered_rendesvous = offer_rendesvous(controller)
		logging.info("Access rendesvous on: http://%s.onion" % offered_rendesvous)
		crier.run(port=5000,debug=True)
	except:
		traceback.print_exc()
	finally:
		logging.info("Komento - shutdown.")
		logging.debug("ending mongo")
		shutdown(box,client)
		logging.debug("Removing rendesvous")
		controller.from_port().remove_ephemeral_hidden_service(offered_rendesvous)
		logging.debug("exiting controller")
		controller.close()
		logging.debug("stopping tor")
		stop_tor()
