#!/usr/bin/python
# coding: utf-8
import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

with open('hosts.txt', 'r') as hosts:
    hostList=hosts.read()

html = """<!DOCTYPE html>
<head>
    <title>C2</title>
</head>
<body>
"""+hostList+"""
</body>
</html>
"""
print(html)

# améliorable pour avoir des liens cliquables et sur plusieurs lignes
