from Classes.PlayableCharacter import PlayableCharacter
from Classes.DiscordUser import DiscordUser

class Customer:
    def __init__(self, data: dict = None):
        if data is not None:
            self._id = data["CGOrder"].get("id")
            self._character = PlayableCharacter(data.get("PlayableCharacter"))
            self._discord_info = DiscordUser(data.get("DiscordUser"))
        else:
            self._id = None
            self._character = None
            self._discord_info = None

    @property
    def id(self):
        return self._id

    @property
    def character(self):
        return self._character

    @property
    def discord_info(self):
        return self._discord_info

    @id.setter
    def id(self, value):
        self._id = value

    @character.setter
    def character(self, value):
        self._character = value

    @discord_info.setter
    def discord_info(self, value):
        self._discord_info = value
