class DiscordUser:
    def __init__(self, data: dict = None):
        if data is not None:
            self._id = data.get("id")
            self._username = data.get("username")
        else:
            self._id = None
            self._username = None

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @id.setter
    def id(self, value):
        self._id = value

    @username.setter
    def username(self, value):
        self._username = value
