class Customer:
    def __init__(self, id, character, discord_info):
        self._id = id
        self._character = character
        self._discord_info = discord_info

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
