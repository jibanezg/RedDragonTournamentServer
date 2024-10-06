from enum import Enum


class RequestType(Enum):
    CREATE_ROOM = 'CREATE_ROOM'
    JOIN_ROOM = 'JOIN_ROOM'


class SocketType(Enum):
    SERVER = 'SERVER'
    CLIENT = 'CLIENT'
