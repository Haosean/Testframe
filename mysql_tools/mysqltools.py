# coding:utf-8
import MySQLdb
from MySQLdb import cursors
# setting mysql
user = 'root'
passwd = '123456'
host = '127.0.0.1'
db = 'bookstore'


class myOperating():
    def __init__(self,
                 user=user,
                 passwd=passwd,
                 host=host, db=db):
        try:
            self.con = MySQLdb.connect(
                host=host, user=user, passwd=passwd, db=db, cursorclass=MySQLdb.cursors.DictCursor)
            print user, passwd, host, db
        except MySQLdb.Error, e:
            print "mysql err %d:%s" % (e.args[0], e.args[1])

    def execQuary(self, sql):
        cur = self.con.cursor()
        res = cur.execute(sql)
        resultlist = cur.fetchall()
        self.con.close()
        return resultlist


def cc():
    sql = "select gst_id,gst_user from book"
    c = myOperating()
    cx = c.execQuary(sql)
    for x in cx:
        print x


cc()
