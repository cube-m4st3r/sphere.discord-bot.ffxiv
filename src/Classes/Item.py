class Item:
    def __init__(self, id, name, description, isCollectable):
        self._id = id
        self._name = name
        self._description = description
        self._isCollectable = isCollectable

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def isCollectable(self):
        return self._isCollectable

    @id.setter
    def id(self, value):
        self._id = value

    @name.setter
    def name(self, value):
        self._name = value

    @description.setter
    def description(self, value):
        self._description = value

    @isCollectable.setter
    def isCollectable(self, value):
        self._isCollectable = value
