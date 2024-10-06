from abc import ABC, abstractmethod

from core.matchmaker import Matchmaker


class Request:

    def __init__(self, socket, data):
        self.__socket = socket
        self.__data = data

    @property
    def socket(self):
        return self.__socket

    @property
    def data(self):
        return self.__data


class RequestHandlerCommand(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass


class CreateRoomRequestHandler(RequestHandlerCommand):

    def __init__(self):
        self.__matchmaker = Matchmaker()

    def handle_request(self, request):
        print(f"Handling Matchmaking request: {request}")


class JoinRoomRequestHandler(RequestHandlerCommand):

    def __init__(self):
        self.__matchmaker = Matchmaker()

    def handle_request(self, request):
        print(f"Handling Matchmaking request: {request}")


class RequestProcessor:

    def __init__(self):
        self.__handler_map = {
            'CREATE_ROOM': CreateRoomRequestHandler(),
            'JOIN_ROOM': JoinRoomRequestHandler()
        }

    def process_request(self, request: Request):
        self.__handler_map[request.data['requestType']].handle_request(request)
