#coding:utf-8

import http.server
import socketserver


port = 80
address = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print("serverhttp.py start on port{port}")
httpd.serve_forever()