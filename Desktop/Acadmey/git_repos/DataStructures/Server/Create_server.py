import http.server 
import socketserver 

PORT = 8080 
handler = http.server.SimpleHTTPRequestHandler
print("hello")
#handler.do_GET("C:\Users\abhisheksingh75\eclipse-workspace\index.html")
httpd = socketserver.TCPServer(('127.0.0.1',PORT), handler, True)
print("server is listing")
httpd.serve_forever()

