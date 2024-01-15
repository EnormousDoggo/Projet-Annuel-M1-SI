#!/usr/bin/python
# coding: utf-8
import cgi
import os

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html></html>"""

with open('hosts.txt', 'a') as hosts:
    hosts.write(form.getvalue("name")+" "+os.environ["REMOTE_ADDR"]+"\n")
