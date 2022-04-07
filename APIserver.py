from io import BytesIO
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("db.json") as data_file:
	data = json.load(data_file)

class myhandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        length = int(self.headers.get('Content-Length'), 0)
        content = self.rfile.read(length)
        temp = str(content).strip('b\'')
        self.end_headers()
        return temp

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=4, separators=(',', ': ')).encode('utf-8'))
        return

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'), 0)
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers
        response = BytesIO()
        response.write(b'This is a POST request.')
        response.write(b'Recieved: ')
        response.write(body)
        self.wfile.write(response.getvalue())

    # def do_PUT(self):
    # def do_DELETE(self):

PORT = 8000

try:
    server = HTTPServer(('localhost', PORT), myhandler)
    print("server running")
    server.serve_forever()
    
except KeyboardInterrupt:
    server.server_close()
    print("server stopped")
