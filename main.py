from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "application/json")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes("{' Hello, World wide web!': 'OK'}", "utf-8"))  # Тело ответа

    def do_POST(self):
        """Метод обработки входящих POST-запросов"""
        c_len = int(self.headers.get('Content-Length'))
        client_data = self.rfile.read(c_len)
        print(client_data)
        self.send_response(201)
        self.send_header("Content-type", "application/json")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа



if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
