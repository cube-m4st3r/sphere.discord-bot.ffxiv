class PlayableCharacter:
    def __init__(self, data: dict = None):
        if data is not None:
            self._id = data.get("id")
            self._name = data.get("name")
            self._last_name = data.get("last_name")
            self._lodestone_url = data.get("lodestone_url")
            self._world = data.get("world")
        else:
            self._id = None
            self._name = None
            self._last_name = None
            self._lodestone_url = None
            self._world = None

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

    def _split_full_name(self, full_name: str):
        if full_name:
            names = full_name.split()
            if len(names) > 1:
                self._name = names[0]
                self._last_name = " ".join(names[1:])
            else:
                self._name = names[0]
                self._last_name = ""
        else:
            self._name = None
            self._last_name = None