#!/usr/bin/python
# encoding: utf-8
 
import os 
import time 
import datetime
import MySQLdb

#config vars 
dbuser = "root"
dbpwd = ""
dbhost = "localhost"
workdir = "/var/backups"
socket = ""
today = (datetime.datetime.today()).strftime("%Y%m%d")
yesterday = (datetime.datetime.today() - datetime.timedelta(1)).strftime("%Y%m%d")
the_day_before_yesterday = (datetime.datetime.today() - datetime.timedelta(2)).strftime("%Y%m%d")
def dumpdb(dbname): 
    sqlvalformat = '''mysqldump --single-transaction %s >%s'''
    tarvalformat = '''tar --directory=%s -zcvf %s %s'''
    dumpfile = os.path.join(workdir, dbname + today + ".sql")
    if os.path.isfile((os.path.join(workdir, dbname + the_day_before_yesterday + ".tar.gz"))):
    	os.remove(os.path.join(workdir, dbname + the_day_before_yesterday + ".tar.gz"))# delete the day before yesterday mysql backup file 
    zipfile = os.path.join(workdir, dbname + today + ".tar.gz")
    sqlval = sqlvalformat % (dbname, dumpfile) 
    result = os.system(sqlval) 
    tarval = tarvalformat % (workdir, zipfile, dbname + today + ".sql") 
    result = os.system(tarval) 
    os.remove(dumpfile)
def dumpdb_all(dbname='all_databases'): 
    sqlvalformat = '''mysqldump --single-transaction --all-databases >%s'''
    tarvalformat = '''tar --directory=%s -zcvf %s %s'''
    dumpfile = os.path.join(workdir, dbname + today + ".sql")
    if os.path.isfile((os.path.join(workdir, dbname + the_day_before_yesterday + ".tar.gz"))):
    	os.remove(os.path.join(workdir,dbname + the_day_before_yesterday + ".tar.gz"))# delete the day before yesterday mysql backup file 
    zipfile = os.path.join(workdir, dbname + today + ".tar.gz")
    sqlval = sqlvalformat % (dumpfile) 
    result = os.system(sqlval) 
    tarval = tarvalformat % (workdir, zipfile, dbname + today + ".sql") 
    result = os.system(tarval) 
    os.remove(dumpfile)

def main(): 
    dbConn = MySQLdb.connect(host=dbhost, port=3306, user=dbuser, passwd=dbpwd)
    cur = dbConn.cursor()
    cur.execute('show databases')
    
    for dbname in cur.fetchall(): 
        dumpdb(dbname[0]) 
    #dumpdb_all('all_databases')
if __name__ == '__main__':
    main()

# crontab -e
# * 1 * * * python /root/python/backup_db.py