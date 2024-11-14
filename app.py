from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello DTSkill")

# Set the server to listen on port 8000
port = 8000
server_address = ("", port)

# Create and start the HTTP server
httpd = HTTPServer(server_address, HelloHandler)
print(f"Serving on port {port}...")
httpd.serve_forever()
#commit 