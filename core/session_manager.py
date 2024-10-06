class SessionManager:

    def __init__(self):
        self.__sessions = {}

    def create_new_session(self, data):
        print("New session created.")


class Session:

    def __init__(self, session_id, **kwargs):
        self.__session_id = session_id
        self.__login_status = kwargs.get('login_status')
        self.__session_history = kwargs.get('session_history')
