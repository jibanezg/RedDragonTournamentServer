class Matchmaker:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Matchmaker, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '__initialized'):
            self.__rooms = {}
            self.__initialized = True

    def create_room(self):
        print(f'Room created')

    def join_room(self):
        print(f'Room joined')
