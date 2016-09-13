import MySQLdb
import mysqlDBOperation

try:
    # conn = MySQLdb.connect(host='fuyidb.cligbfk3fwfi.ap-northeast-2.rds.amazonaws.com',
    #                        user='zhangyw', passwd='tsusaka312', db='fuyiDB', port=3306, charset='utf8')
    conn_aws = mysqlDBOperation.newconnection('fuyidb.cligbfk3fwfi.ap-northeast-2.rds.amazonaws.com', 3306,
                                              'zhangyw', 'tsusaka312', 'fuyiDB', 'utf8')

    conn_local = mysqlDBOperation.newconnection('s3760i.mars.grid.sina.com.cn', 3760,
                                                'gina_mis', 'L9Xy5RbtXe3u3Zu7AZwWm039yIN19H4r', 'gina', 'utf8')

    print 'connection successful!'

    cur_local = mysqlDBOperation.exesql(conn_local, 'select * from agent')

    # get table"agent" data
    agents = mysqlDBOperation.fetchalldata(cur_local)

    # print top 10 elements
    # for ag in agents[:10]:
    #     print ag

    cur_aws = mysqlDBOperation.exesql(conn_aws, 'select count(*) from agent')
    rownum = mysqlDBOperation.fetchalldata(cur_aws)
    if rownum == 0:
        mysqlDBOperation.exesql(conn_aws, 'truncate table agent')

    sql = 'insert into agent(agent_id, name, full_name, contact_name, address, tel, city,' \
          ' update_time, create_time, start_time, end_time, status, type, user, industry_id,' \
          ' region, portal_contract, weibo_contract, org_id, version) values (%s, %s, %s, %s, %s, %s, %s,' \
          ' %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    result = cur_aws.executemany(sql, agents)
    print 'insert agent', result

    conn_aws.commit()

    mysqlDBOperation.closecursor(cur_aws)
    mysqlDBOperation.closecursor(cur_local)
    mysqlDBOperation.closeconnection(conn_aws)
    mysqlDBOperation.closeconnection(conn_local)
    print 'connection closed!'
except MySQLdb.Error, e:
    print 'Mysql Error %d: %s' % (e.args[0], e.args[1])
