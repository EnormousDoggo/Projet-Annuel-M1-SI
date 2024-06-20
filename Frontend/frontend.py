import http.server
import socketserver

PORT = 8000

# Set the handler to the class we created
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
