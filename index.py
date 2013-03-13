#!/usr/bin/env python


#imports
import bottle
import urllib2
import simplejson
import pymysql

from bottle import route

#db
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='fb')
cur = connection.cursor()

#globals
base = "http://bowd.in"
MAX_INCREASE = 32

@route('/assets/:filename')
def static(filename):
	return bottle.static_file(filename, root='assets/')
	
@route('/assets/:sub/:filename')
def static(sub,filename):
	return bottle.static_file(filename, root='assets/%s/'%sub)
	
@route('/')
def index():
	cur.execute("SELECT fbid,name FROM main ORDER BY wins DESC LIMIT 24")
	data = cur.fetchall();
	k = []
	for d in data:
		k.append(tuple(["http://graph.facebook.com/"+str(int(d[0]))+"/picture?type=large", str(d[1])]))
	return bottle.template("views/welcome", top = k)
	
@route('/iam/:sex')
def game(sex):
	if(sex == 'female' or sex == 'male'):	
		if sex == 'female': s = 'male'
		if sex == 'male': s = 'female' 
		return bottle.template('game', gender = s)
	else:
		bottle.redirect('/')
	
	
@route('/send/:sex')
def show(sex):
	if(sex == 'female' or sex == 'male'):
		cur.execute("SELECT fbid,wins,matches FROM main WHERE sex = '%s' ORDER BY RAND() LIMIT 2"%sex)
		r = cur.fetchall()
		d = []
		for i in r:
			d.append(int(i[0]))
			d.append(int(i[1]))
		return simplejson.dumps(d)
	else:
		bottle.redirect('/')
		
@route('/game/:a/wins/:b',method='GET')
def match(a,b):
	global MAX_INCREASE
	'''
	A match where a defeated b. a,b E (fbids)
	'''
	cur.execute("SELECT * FROM main WHERE fbid = %s"%a)
	ia = list(cur.fetchone())
	
	cur.execute("SELECT * FROM main WHERE fbid = %s"%b)
	ib = list(cur.fetchone())
	
	#i* is something of form (1L, 4L, 'male', 1500L, 0L, 0L)
	
	#calculate effective change in score
	e2 = MAX_INCREASE * 1 / (1 + 10 ** (( int(ia[3]) - int(ib[3])) / 400))
	
	#increment matches
	ia[5] = int(ia[5]) + 1
	ib[5] = int(ib[5]) + 1
	
	#now a has won
	ia[3] = int(ia[3]) + e2
	ia[4] = int(ia[4]) + 1 #increment wins
	
	ib[3] = int(ib[3]) - e2
	
	#return str(ia) + " \n\n  "+str(ib)
	cur.execute("UPDATE main SET score=%s, wins=%s, matches=%s WHERE fbid=%s"%(ia[3], ia[4], ia[5], a))
	cur.execute("UPDATE main SET score=%s, wins=%s, matches=%s WHERE fbid=%s"%(ib[3], ib[4], ib[5], b))
	connection.commit()
	return simplejson.dumps(True)
	
@route('/leaders')
def leaders():
	cur.execute("SELECT * FROM main ORDER BY wins DESC LIMIT 10")
	return str(cur.fetchall())
	
@route('/faq')
def faq():
	return bottle.template('views/faq')	
	
@route('/report')
def report():
	bottle.redirect('https://docs.google.com/forms/d/1iLs4-PJSBR0vjKe4eF9xi64BF9CiAjVrCW5hHAuRlqU/viewform')
	
@route('/contact')
def contact():
	bottle.redirect('https://docs.google.com/forms/d/1lub_oz5sTr7iOXF6TG6TEj-g4Y2cGEB_iFFYlYGI5T0/viewform')
	
	
bottle.debug(True)
bottle.run(reloader = True, port=8000)
