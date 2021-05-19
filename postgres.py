#!/usr/bin/python
# coding: utf-8

"""
Module for work with DB PostgreSQL: postgres.py
"""
from __future__ import print_function
import os
import psycopg2
import allure

DB_PASS = os.environ["DB_PASS"]

def select_from(table, field, test_id, insikt_dbname='insikt', insikt_host='1'):
    """select from table"""
    sql = 'SELECT ' + field + ' FROM ' + table +' WHERE id = ' + test_id +';'
#    sql = 'SELECT ' + field + ' FROM ' + table +" WHERE id = \'3\'" +';'

    try:
        insikt_dbpassword = DB_PASS
        conn = psycopg2.connect("dbname=" + insikt_dbname + " host=" + insikt_host + \
" user=postgres password=" + insikt_dbpassword)
        cur = conn.cursor()
        cur.execute(sql, test_id)
        conn.commit()
        row = cur.fetchone()
        cur.close()
    except (psycopg2.DatabaseError) as error:
        print('error_db', error)
    finally:
        if conn is not None:
            conn.close()

    return row[0]


def update_server(server, port, link, state, insikt_dbname='insikt', insikt_host='localhost'): \
#pylint: disable-msg=too-many-arguments
    """ update server state based on the server, port, link """
    sql1 = """ INSERT INTO servers ( state, server, port, link )
                VALUES ( %s, %s, %s, %s )
                ON CONFLICT ON CONSTRAINT servers_server_port_link_key
                DO NOTHING; """
#                DO UPDATE
#SET work = EXCLUDED.work || ';' || servers.server || ':' || servers.port || '/' || servers.link;"""
    sql2 = """ UPDATE servers
                SET state = %s
                WHERE server = %s
                AND port = %s
                AND link = %s ;"""
    conn = None
    update_rows = 0
    try:
        insikt_dbpassword = DB_PASS
        conn = psycopg2.connect("dbname=" + insikt_dbname + " host=" + insikt_host + \
" user=postgres password=" + insikt_dbpassword)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS servers (id serial \
PRIMARY KEY, state integer, server varchar, \
port integer, link varchar, work varchar, UNIQUE (server, port, link));")
        cur.execute("CREATE TABLE IF NOT EXISTS api (id serial PRIMARY KEY, state integer, \
host varchar, port integer, rest varchar, link varchar, header varchar, input varchar, \
output varchar);")
        conn.commit()
        cur.execute(sql1, (state, server, port, link))
        conn.commit()
        cur.execute(sql2, (state, server, port, link))
        update_rows = cur.rowcount
        allure.attach('rowcount', update_rows)
        conn.commit()
        cur.close()
#    except (Exseption, psycopg2.DatabaseError) as error:
    except (psycopg2.DatabaseError) as error:
        allure.attach('error_db', error)
    finally:
        if conn is not None:
            conn.close()

    return update_rows

def main():
    """ Todo nathing"""
    pass

if __name__ == "__main__":
    main()
