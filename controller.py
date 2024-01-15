#!/usr/bin/python

from requests import get
import http.server
 
PORT = 8888
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
httpd = server(server_address, handler)


print("Serveur actif sur le port :", PORT)
httpd.serve_forever()