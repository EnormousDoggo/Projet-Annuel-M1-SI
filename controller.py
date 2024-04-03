#!/usr/bin/python

import http.server
import cgitb;

cgitb.enable()  # Error reporting
 
PORT = 8888
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
httpd = server(server_address, handler)


print("Serveur actif sur le port :", PORT)
httpd.serve_forever()
