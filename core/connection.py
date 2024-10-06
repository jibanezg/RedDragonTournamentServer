class Connection:

    def __init__(self, client_socket, client_address):
        self.__client_socket = client_socket
        self.__client_address = client_address
