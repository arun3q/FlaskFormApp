import pymysql 

def connection():
	conn = pymysql.connect(host="localhost", user='root', passwd='pass', db='users_data')
	c = conn.cursor()
	return c, conn
