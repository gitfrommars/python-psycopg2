#!/usr/bin/python
import psycopg2
import smtplib
import os
import sys
import re
import commands
import time
import subprocess


def connect_db():
    try:
        conn = psycopg2.connect("dbname='DBN' user='U' host='H'  port='P' password='P'")
# conn = psycopg2.connect("dbname='' user='' host=''  port='' password=''"
        conn.close()
        return True
    except:
        return False

while True:
    print "%s" % time.ctime() + " - " + str(connect_db())
    time.sleep(1)

sys.exit(0)

