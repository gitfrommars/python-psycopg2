#!/usr/bin/python
import psycopg2
import smtplib
import os
import sys
import re
import commands
import time
import subprocess

def  connect_db( ):	
    try:
        conn = psycopg2.connect("dbname='valemobi' user='Valemobi' host='10.208.96.105'  port='5432' password=''")
#        conn = psycopg2.connect("dbname='valemobi' user='Valemobi' host='192.168.80.201'  port='15432' password=''")
        conn.close()
        return True
    except:
        return False





while True: 
    print  "%s" % time.ctime() + " - " +  str(connect_db())   
    time.sleep(1)




sys.exit(0)
