from pymongo import MongoClient
aclient = MongoClient("172.18.0.2", 27017)
users = aclient.delegito.users
records = aclient.delegito.records
from emails import mail

from keyvalues import remove_active, make_active
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
