#!/usr/bin/env python


#imports
import pymysql
import urllib2
import simplejson

#globals
base = "http://graph.facebook.com/"

#db
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='fb')
cur = connection.cursor()

#crawl
def add_to_db(fbid, sex, name):
	sql = "INSERT INTO main (fbid, sex, score,wins, matches, name) VALUES (%s, '%s', 1500,0, 0, %s)"%(fbid,sex, name)
	cur.execute(sql)
	connection.commit()

	
def get_last_id():
	cur.execute("SELECT MAX(fbid) FROM main")
	a = cur.fetchone()
	return int(a[0])
	
def put(index):	
  #print "Trying " + str(index)
	try:
		req = urllib2.Request(base+str(index))
		opener = urllib2.build_opener()
		f = simplejson.load(opener.open(req))
		if f.has_key('id'):
			add_to_db(int(f['id']), f['gender'], f['name'])
			print "Hit " + str(index) + "\n"
			put(index + 1)
	except:
		put(index + 1)

def get_names():
	cur.execute("SELECT fbid FROM main WHERE name='0'")
	fbids = cur.fetchall()
	for i in fbids:
		i = int(i[0])
		try:
			req = urllib2.Request(base+str(i))
			opener = urllib2.build_opener()
			f = simplejson.load(opener.open(req))
			name = f['name']
			print str(i)+ "  "+name
			try:
				cur.execute("""UPDATE main SET name="%s" WHERE fbid=%s"""%(name,i))
				connection.commit()
			except:
				pass
		except:
			pass		
		
		
def set_urls():
	cur.execute("SELECT fbid FROM main")
	fbids = cur.fetchall()
	for i in fbids:
		i = int(i[0])
		url = "http://graph.facebook.com/"+str(i)+"/picture?type=large"	
		cur.execute("""UPDATE main SET url="%s" WHERE fbid=%s"""%(url,i))
		connection.commit()
		print "set %s"%i
#get_names()
#put(get_last_id() + 1)
set_urls()
#cur.execute("INSERT INTO main (fbid, sex, score,wins) VALUES (5, 'm', 1500,0)")

