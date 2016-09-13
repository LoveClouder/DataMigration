import MySQLdb


def newconnection(host, port, user, passwd, defaultdb, charset):
    conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=defaultdb, charset=charset)
    return conn


def closecursor(cursor):
    cursor.close()


def closeconnection(conn):
    conn.close()


def exesql(conn, sqltext):
    if conn.open is False:
        conn.open()
    cur = conn.cursor()
    cur.execute(sqltext)
    return cur


def fetchalldata(cursor):
    data = cursor.fetchall()
    return data


if __name__ == '__main__':
    print 'no executive module mysqlDBOperation.'
