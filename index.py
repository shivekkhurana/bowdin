#!/usr/bin/env python
import sys
sys.path.insert(0,'/home/bowdin/webapps/bowdin/lib/python2.7')

#imports
import bottle
try:
    import simplejson
except:
	import json as simplejson
import pymysql

from bottle import route
from bottle import error

#db
#connection = pymysql.connect(host='mysql.server', port=3306, user='shivekkhurana', passwd='h3licopter', db='shivekkhurana$default')
#connection = pymysql.connect(host='localhost', port=3306, user='shivekkhurana', passwd='h3licopter', db='fb')
#cur = connection.cursor()
connection = cur = 0

def db_open():
    global connection, cur
    connection = pymysql.connect(host='mysql.server', port=3306, user='shivekkhurana', passwd='h3licopter', db='shivekkhurana$default')
    cur = connection.cursor()

def db_close():
    global connection,cur
    #cur.close()
    #connection.close()

#globals
base = "http://bowd.in"
MAX_INCREASE = 32

bottle.TEMPLATE_PATH.insert(0,'/home/bowdin/webapps/bowdin/htdocs/')

'''
@route('/assets/:filename')
def static(filename):
	return bottle.static_file(filename, root='assets/')

@route('/assets/:sub/:filename')
def static2(sub,filename):os.system("/home/you/webapps/your_app/apache2/bin/restart")

time.sleep(3)
	return bottle.static_file(filename, root='assets/%s/'%sub)
'''

@route('/')
def index():
    global connection, cur
    db_open()
    cur.execute("SELECT url, name, score FROM main  WHERE fbid > 399999 ORDER BY score DESC LIMIT 24")
    data = cur.fetchall()
    db_close()
    k = []
    for d in data:
		k.append(tuple([str(d[0]), str(d[1]), int(d[2])]))
    db_close()
    return bottle.template("views/welcome", top = k)

@route('/iam/:sex')
def game(sex):
	if(sex == 'female' or sex == 'male'):
		if sex == 'female': s = 'male'
		if sex == 'male': s = 'female'
		return bottle.template('views/game', gender = s)
	else:
		bottle.redirect('/')


@route('/send/:sex')
def show(sex):
    if(sex == 'female' or sex == 'male'):
        db_open()
        cur.execute("SELECT fbid,wins,url FROM main WHERE sex = '%s' AND fbid > 399999 ORDER BY matches, RAND() LIMIT 30"%sex)
        r = cur.fetchall()
        db_close()
        d = []
        t = []
        for i in r:
			t.append(int(i[0]))
			t.append(int(i[1]))
			t.append(i[2])
			d.append(t)
			t=[]
        return simplejson.dumps(d)
    else:
		bottle.redirect('/')

@route('/game/:a/wins/:b',method='POST')
def match(a,b):
    global MAX_INCREASE
    '''
	A match where a defeated b. a,b E (fbids)
	'''
    db_open()
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
    db_close()

    return simplejson.dumps(True)

#@route('/leaders')
#def leaders():
#	cur.execute("SELECT * FROM main ORDER BY wins DESC LIMIT 10")
#	return str(cur.fetchall())

@route('/faq')
def faq():
	return bottle.template('views/faq')

@route('/report')
def report():
	bottle.redirect('https://docs.google.com/forms/d/1iLs4-PJSBR0vjKe4eF9xi64BF9CiAjVrCW5hHAuRlqU/viewform')

@route('/contact')
def contact():
	bottle.redirect('https://docs.google.com/forms/d/1lub_oz5sTr7iOXF6TG6TEj-g4Y2cGEB_iFFYlYGI5T0/viewform')

@route('/del/:src')
def d(src):
	#cur.execute("DELETE FROM main WHERE fbid>=404595")
	#connection.commit()
	#db_refresh()os.system("/home/you/webapps/your_app/apache2/bin/restart")
	pass

@route('/monitor')
def monitor():
	#global connection
	pass

#cur.execute("SELECT fbid,url, wins, score, matches FROM main Where fbid>404461 AND sex='male'")
#	a = cur.fetchall()
#	db_refresh()
	#b = "fbid,url, wins, score, matches<style type='text/css'>img{max-width:150px;width:150px;}</style>"
	#for i in a:
	#	b = b+ str(i) + "<a href=/del/"+str(i[0])+"><img src='"+i[1]+"'></a>"
	#return str(b)


@error(404)
def error404(error):
    return '<h1>Hello, we screwed up your request.</h1><br/>Tecnically its called an <i>404:not found error</i>.<br/><a href="/" alt="home">Return to Home Page</a> '

@error(500)
def error500(error):
	return '<h1>Hello, we screwed up your request.</h1><br/>Tecnically its called an <i>500:server error</i>.<br/><a href="/" alt="home">Return to Home Page</a> '

@route('/server_')
def refresh():
	from os import system
	system("/home/you/webapps/your_app/apache2/bin/restart")
	import time
	time.sleep(3)
	return "true"
	#from subprocess import call
	#return call(["ls"]) #call(["cd /home/bowdin/webapps/bowdin/apache2/bin ;./restart"])

#bottle.debug(True)
#bottle.run(reloader = True)
application = bottle.default_app()
