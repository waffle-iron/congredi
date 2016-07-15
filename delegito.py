#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, json, Response,render_template, session, request, redirect, url_for, escape
from structs.keyvalues import *
from structs.mongos import *
from structs.emails import *
#from structs.delegito import Learner, Crypto

def userdata(request,e=True):
    j = request.get_json()
    print j
    # required fields (could for loop this)
    # validate & escape fields for db
    try: username = j['username']
    except: raise Exception('Username Required')
    try: password = j['password']
    except: raise Exception('Password Required')
    if e:
        try: email = j['email']
        except: raise Exception('Email Required')
        return username, password, email
    return username, password
app = Flask('Delegito')
@app.route('/api/auth/',methods=['POST','DELETE'])
def db_authorize():
    ac = request.method
    if ac == 'POST':
        u, p, e = userdata(request)
        mid = mongo_start(u, p, e)
        if 'error' not in mid.keys():
            token = mongo_token(u,p)
            response = make_active(token,secret)
        else: response = mid
        return jsonify(response)
    elif ac == 'DELETE':
        u, p = userdata(request,e=False)
        mid = check_active(request,secret)
        if 'error' not in mid.keys():
            mid = mongo_stop(u,p)
            if 'error' not in mid.keys():
                response = remove_active(mid)
            else: response = mid
        else: response = mid
        return jsonify(response)
@app.route('/api/token/',methods=['GET','DELETE'])
def session_control():
    ac = request.method
    if ac == 'GET':
        username, password = userdata(request,e=False)
        mid = mongo_token(username,password)
        if 'error' not in mid.keys():
            response = make_active(username,secret)
        else: response = mid
    elif ac == 'DELETE':
        mid = check_active(request,secret)
        if 'error' not in mid.keys():
            response = remove_active(mid)
        else: response = mid
    return jsonify(response)
# like... oauth2?
@app.route('/api/bearing/',methods=['GET'])
def long_bearer():
    # records.find(query).skip(offset).limit(limit)
    username, password = userdata(request,e=False)
    mid = check_active(request,secret)
    if 'error' not in mid.keys():
        make_active(username,secret,bearing=True)
    else:
        result = mid
    return jsonify(result)
@app.route('/api/search/<recordType>',methods=['GET'])
def search_mongo(recordType):
    # records.find(query).skip(offset).limit(limit)
    mid = check_active(request,secret)
    if 'error' not in mid.keys():
        query = request.get_json()['query']
        if recordType == 'users':
            result = users.find_one({recordType:query})
        elif recordType == 'records':
            result = records.find_one({recordType:query})
        if result is None:
            result = {'info':'Nothing by that name...'}
    else:
        result = mid
    return jsonify(result)
@app.route('/api/storage/<recordType>/<uuid>',methods=['GET','POST','PUT','UPDATE'])
def executeIO(recordType,uuid):
    mid = check_active(request,secret)
    if 'error' not in mid.keys():
        ac = request.method
        if ac == 'GET':
            query = request.get_json()['query']
            if recordType == 'users':
                result = users.find_one({recordType:query})
            elif recordType == 'records':
                result = records.find_one({recordType:query})
        else:
            record = request.get_json()
            if ac == 'POST':
                if recordType == 'users':
                    users.push_one(query)
                elif recordType == 'records':
                    records.push_one(query)
                result = {'success':'successfully added'}
            else:
                if recordType == 'users':
                    users.update_one(query)
                elif recordType == 'records':
                    records.update_one(query)
                result = {'success':'successfully updated'}
        if result is None:
            result = {'info':'Nothing by that name...'}
    else: result = mid
    return jsonify(result)

@app.errorhandler(404)
def not_found(error):
    print('route: error')
    from flask import make_response
    return make_response(jsonify( { 'error': 'Notfound' } ), 404)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
#http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
#https://pypi.python.org/pypi/Flask-Zurb-Foundation/0.2.1
#https://pypi.python.org/pypi/premailer/