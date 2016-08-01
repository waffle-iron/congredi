import jwt, datetime
def check_active(request, secret): # no redis smarts at all
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
def make_active(username, secret, bearing=False):
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
