#!/usr/bin/python3
"""
Module containing a simple HTTP server.
"""
import http.server, socketserver, json


PORT = 8000
class MyWebServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            string = 'Hello, this is a simple API!'
            self.wfile.write(string.encode())

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(data.encode())

        elif self.path == '/status':
            self.send_response(200)
            self.end_headers()
            self.wfile.write('OK'.encode())
        else:
            self.send_error(404)

def start_server():
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(('', PORT), MyWebServer) as httpd:
        print('Now serving on PORT ', PORT)
        httpd.serve_forever()

start_server()
