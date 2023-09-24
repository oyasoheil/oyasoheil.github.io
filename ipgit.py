import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open('index.html', 'r') as f:
            self.wfile.write(f.read().encode('utf-8'))

PORT = 8000

server = socketserver.TCPServer(('localhost', PORT), MyHandler)

server.serve_forever()
