import os
import random
import sys
import subprocess
import psycopg2
from datetime import datetime
from time import sleep

filename = "app.log" 
f = subprocess.Popen(['tail','-F',filename],
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)

while True:
    
    line = f.stdout.readline()
    if "ERR" in line:
        print "ini eror pada "+str(datetime.now())
        try:
            conn = psycopg2.connect(database="syslog", user="fenaldy", password="salman", host="127.0.0.1", port="5432")
            cur = conn.cursor()
            now = str(datetime.now())
            messages = line[32:]
            cur.execute("INSERT INTO test_log (event_date, messages)VALUES (%s, %s)",(now, messages))
            conn.commit()
            cur.close()
            conn.close()
        except:
            print "cant insert"