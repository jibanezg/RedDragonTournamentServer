import selectors
import socket

from core.enums import RequestType, SocketType
from core.request_processor import RequestProcessor, Request
from core.session_manager import SessionManager


class Server:

    def __init__(self, **kwargs):
        self.__server_name = kwargs.get('server_name')
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__selector = selectors.DefaultSelector()
        self.__session_manager = SessionManager()
        self.__request_processor = RequestProcessor()

    def start_server(self, host='127.0.0.1', port=8080):
        self.__server_socket.bind((host, port))
        self.__server_socket.listen()
        print(f'Server listening on port: {port}')
        self.__server_socket.setblocking(False)
        data = {
            'socketType': SocketType.SERVER
        }
        self.__selector.register(self.__server_socket, selectors.EVENT_READ, data=data)

    def __accept_connection(self, server_socket):
        conn, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        data = {
            'socketType': SocketType.CLIENT
        }
        self.__selector.register(conn, selectors.EVENT_READ, data=data)

    def run(self):
        try:
            request_processor = RequestProcessor()
            while True:
                for key, mask in self.__selector.select():
                    socket_type = key.data['socketType']
                    if socket_type is SocketType.SERVER:
                        self.__accept_connection(key.fileobj)
                    else:
                        request = Request(key.fileobj, key.data)
                        request_processor.process_request(request)
        except KeyboardInterrupt:
            print("Server shutting down.")
        finally:
            self.__selector.close()


if __name__ == '__main__':
    game_server = Server()
    game_server.start_server()
    game_server.run()
