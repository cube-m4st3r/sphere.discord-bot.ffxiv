class DiscordUser:
    def __init__(self, data: dict = None):
        if data is not None:
            self._id = data.get("id")
            self._username = data.get("username")
            self._avatarUrl = data.get("avatarUrl")
        else:
            self._id = None
            self._username = None
            self._avatarUrl = None

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username
    
    @property
    def avatarUrl(self):
        return self._avatarUrl

    @id.setter
    def id(self, value):
        self._id = value

    @username.setter
    def username(self, value):
        self._username = value

    @avatarUrl.setter
    def avatarUrl(self, value):
        self._avatarUrl = value
