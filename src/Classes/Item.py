class Item:
    def __init__(self, data: dict = None):
        if data is not None:
            self._id = data.get("id")
            self._name = data.get("name")
            self._description = data.get("description")
            self._isCollectable = data.get("isCollectable")
            self._isCanBeHQ = data.get("CanBeHQ")
        else:
            self._id = None
            self._name = None
            self._description = None
            self._isCollectable = None
            self._isCanBeHQ = None

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
    
    @property
    def isCanBeHQ(self):
        return self._isCanBeHQ

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

    @isCanBeHQ.setter
    def isCanBeHQ(self, value):
        self._isCanBeHQ
