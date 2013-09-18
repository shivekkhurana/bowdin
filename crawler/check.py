import pymysql
s = open("tb_urls.txt","r").read().split("\n")
fbid = 400000
	
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='fb')
cur = connection.cursor()

#crawl
def add_to_db(fbi, sex, name, url):
	sql = "INSERT INTO main (fbid, sex, score,wins, matches, name, url) VALUES (%s, '%s', 1500,0, 0, '%s','%s')"%(fbi,sex, name,url)
	cur.execute(sql)
	connection.commit()
	
for u in s:
	print u
	#add_to_db(fbid,"female", "Name Unknown",u)
	#fbid +=1


