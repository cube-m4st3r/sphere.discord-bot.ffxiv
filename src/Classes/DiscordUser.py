class DiscordUser:
    def __init__(self, id, username):
        self._id = id
        self._username = username

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
