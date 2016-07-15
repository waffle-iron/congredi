def open_journal():
	connection = MongoClient()
	logging.debug(connection.database_names())
	try:
		db = connection['komento']#.u_s#u-s
		#local.connect()
	except:
		db = client[client.database_names()[0]]
		logging.debug(db.name)
		logging.debug(db.collection_names())
		logging.debug(db.collection_names(include_system_collections=False))
	return connection
def search_journal(context,limits=1,skip=0): #{"key,value"} '_id'
	db = open_journal()
	if limits == 1:
		res = db.komento.find_one(context)
	else:
		if skip == 0:
			res = db.komento.find().limit(limits)
		else:
			res = db.komento.find().limit(limits).skip(skip)
	count = res.count()
	return res, count
def append_journal(document):
	db = open_journal()
	if type(document) is not type(list):
		res = db.komento.insert_one(post)#.inserted_id#.insert()
		return res
	else:
		res = db.komento.insert_many(document)
		return res.inserted_ids
def notes():
	post = {
		"author":"",
		"body":"",
		"precidents":[],
		"fallicies":[],
		"signature":"",
		"date": datetime.datetime.utcnow()
	}
	class BlogPost(Document):
	    title = StringField(required=True, max_length=200)
	    posted = DateTimeField(default=datetime.datetime.now)
	    tags = ListField(StringField(max_length=50))
	post2.save()
	if isinstance(post, TextPost):
		len(LinkPost.objects)
		len(BlogPost.objects(tags='mongodb'))
	for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
		pass
		#[item["x"] for item in result = db.profiles.create_index([('user_id', pymongo.ASCENDING)] unique=True)
	db.collection.create_index("x")
	db.collection.index_information()
# 1. ensure that tor is running
# 2. ensure mongodb is running
# 2. ensure directory is correct
# build files
#https://github.com/GoogleCloudPlatform/getting-started-python
#$ mongod
#https://github.com/theorm/mongobox
def mongols():
	dotfiles = os.path.expanduser('~/.komento/')
	if not os.path.exists(dotfiles):
		print("Creating komento dir.")
		os.mkdir(dotfiles)
	return dotfiles

def shutdown(client):
	client.close()#disconnect()
	#assert not client.alive()
