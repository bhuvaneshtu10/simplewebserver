from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        with open("simplewebserver.html", "r") as f:
            content = f.read()
        self.wfile.write(content.encode())
print("This is my webserver") 
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()