from email.policy import HTTP
import http.server
import socketserver

class myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/myotherpage':
            self.path = 'myotherpage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


port = 5000

handler = myhandler

myserver = socketserver.TCPServer(("", port), handler)
myserver.serve_forever()