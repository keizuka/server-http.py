#coding:utf-8
import http.server
port = 80
address = ("", port)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["index.py"]
httpd = server(address, handler)
print("serverhttp.py start on port ", {port})
httpd.serve_forever()