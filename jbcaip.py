#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import ipaddress
import requests

SERVER_PORT = 18433
SERVER_PATH = "/"

def main():
    webServer = HTTPServer(("", SERVER_PORT), requestHandler)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == SERVER_PATH:
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            ip = self.headers.get("X-Forwarded-For")
            if ipaddress.IPv4Address(ip).is_private:
                self.wfile.write(bytes(requests.get("https://ifconfig.me/ip").text, encoding='utf8'))
            else:
                self.wfile.write(bytes(ip, encoding='utf8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("404 Not Found", encoding='utf8'))

if __name__ == "__main__":
    main()