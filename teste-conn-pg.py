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
        conn = psycopg2.connect("dbname='_@DBNAME@_' user='_@USR@_' host='_@HOST@_'  port='_@PORT@_' password='_@PWD@_'")
# conn = psycopg2.connect("dbname='' user='' host=''  port='' password=''"
        conn.close()
        return True
    except:
        return False

while True:
    print "%s" % time.ctime() + " - " + str(connect_db())
    time.sleep(1)

sys.exit(0)

