import MySQLdb

try:
    conn = MySQLdb.connect(host='fuyidb.cligbfk3fwfi.ap-northeast-2.rds.amazonaws.com',
                           user='zhangyw', passwd='tsusaka312', db='fuyiDB', port=3306, charset='utf8')
    cur = conn.cursor()
    print 'connection successful!'

    cnt = cur.execute('select * from agent limit 10')
    print cnt

    agents = cur.fetchall()

    for ag in agents:
        print ag

    cur.close()
    conn.close()
    print 'connection closed!'
except MySQLdb.Error, e:
    print 'Mysql Error %d: %s' % (e.args[0], e.args[1])