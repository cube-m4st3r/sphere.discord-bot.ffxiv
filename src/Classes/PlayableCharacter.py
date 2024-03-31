class PlayableCharacter:
    def __init__(self, id, name, last_name, lodestone_url, world):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._lodestone_url = lodestone_url
        self._world = world

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name

    @property
    def lodestone_url(self):
        return self._lodestone_url

    @property
    def world(self):
        return self._world

    @id.setter
    def id(self, value):
        self._id = value

    @name.setter
    def name(self, value):
        self._name = value

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @lodestone_url.setter
    def lodestone_url(self, value):
        self._lodestone_url = value

    @world.setter
    def world(self, value):
        self._world = value
