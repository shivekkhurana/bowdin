import re
import urllib2
#import MySQLdb as pymysql

#connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='fb')
#cur = connection.cursor()

websites = ["http://blog_name.tumblr.com/page/"]

f = open("file.html","a+b")

def add_to_db(fbi, sex, name, url):
	#sql = "INSERT INTO main (fbid, sex, score,wins, matches, name, url) VALUES (%s, '%s', 1500,0, 0, '%s','%s')"%(fbi,sex, name,url)
	#cur.execute(sql)
	#connection.commit()
	f.write("<img src='%s'/><br/>"%url)
	#urllib2.urlretrieve(url, str(fbi) + url[-4] +url[-3] + url[-2] + url[-1])
	
fbid =402920+1

for i in range(1,301):
	print i
	s = urllib2.urlopen(websites[0]+str(i)).read()
	a = re.findall(r'(http://2[45].media.tumblr.com/[a-zA-Z0-9_.]*/tumblr_[a-zA-Z0-9_.]*)', s)
	b = re.findall(r'(http://2[45].media.tumblr.com/tumblr_[a-zA-Z0-9_.]*)', s)

	for j in a+b:
		print j
		add_to_db(fbid,"male", "Name Unknown",j)
		fbid +=1
