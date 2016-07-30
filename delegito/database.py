import os, logging, redis, celery, pymongo, datetime#,tensorflow
import jwt
from pymongo import MongoClient
redis.StrictRedis(host='172.18.0.3', port=6379, db=0, password=None, socket_timeout=None, connection_pool=None, charset='utf-8', errors='strict', unix_socket_path=None)
def check_active(request,secret): # no redis smarts at all
    if not request.headers.get('Authorization'):
        response = {'error':'Missing Authorization Token'}
    else:
        token = request.headers.get('Authorization')
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        try:
            payload = jwt.decode(token, secret, algorithms=['HS256'])
            user_id = payload['sub']
            response = {'user_id':user_id}
        except DecodeError:
            response = {'error':'Invalid Token'}
        except ExpiredSignature: #ExpiredSignatureError
            response = {'error':'Expired Token'}
        except:
            response = {'error':'general'}
    if 'error' in response.keys(): print('Invalid Token')
    else: print('Valid Token')
    return response
def make_active(username,secret,bearing=False):
    print('Encoding JSON Web Token')
    iat = datetime.datetime.utcnow()
    # bearing sets session duration
    if bearing: exp = iat + datetime.timedelta(days=7)
    else: exp = iat + datetime.timedelta(days=1)

    payload = {
        'sub': username,
        'iat': iat,
        'exp': exp
        }
    token = jwt.encode(payload, secret, algorithm='HS256')
    return {'Authorization':token.decode('unicode_escape')}
def remove_active(token):
    print('Invalidating JSON Web Token')
    response = {'goodbye':'for now'}
    return response

aclient = MongoClient("172.18.0.2", 27017)
users = aclient.delegito.users
records = aclient.delegito.records

def mongo_start(user,pasw,email):
    if users.find_one({'username':user}) is None:
        if users.find_one({'email':email}) is None:
            users.insert_one({
                'username':user,
                'password':pasw,
                'email':email
                })
            mail(email,'Delegito','account crypto')
            result = {'success':'added username'}
        else:
            result = {'error':'email is taken'}
    else:
        result = {'error':'username is taken'}
    if 'error' in result.keys():
        print(result)
    return result
def mongo_token(user,pasw):
    if users.find_one({'username':user}) is not None:
        print(users.find_one({'username':user}))
        if users.find_one({'username':user})['password'] == pasw:
            print('User may be granted a token.')
            result = {'success':'Authorized user and password'}
        else:
            result = {'error':'password incorrect'}
    else:
        result = {'error':'username does not exist'}
    if 'error' in result.keys():
        print(result)
    return result

def mongo_stop(user,pasw):
    if users.find_one({'username':user}) is not None:
        if users.find_one({'username':user})['password'] == pasw:
            users.delete_one({'username':user})
            print('Deleted user: {}'.format(user))
            result = {'success':'user has been deleted'}
        else:
            result = {'error':'password incorrect'}
    else:
        result = {'error':'username does not exist'}
    if 'error' in result.keys():
        print(result)
    return result
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
