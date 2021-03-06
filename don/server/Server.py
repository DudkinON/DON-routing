from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from don.router.Router import Router
from settings import get_settings


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        run = Router(self.path, get_settings())
        self.wfile.write(run.run_action().encode())

    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        length = int(self.headers.get('Content-length', 0))
        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()
        # 3. Extract the "message" field from the request data.
        message = parse_qs(data)['message'][0]
        print(message)
        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        if message:
            self.wfile.write(message.encode())

    def get_header(self, error):
        self.send_response(error)


def server(ip='127.0.0.1', port=8000):
    print('Server running on ip: {}, and port: {}'.format(ip, port))
    print('http://{}:{}'.format(ip, port))
    httpd = HTTPServer((ip, port), Handler)
    httpd.serve_forever()

if __name__ == '__main__':
    server()
else:
    server = server
