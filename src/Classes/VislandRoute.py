class VislandRoute:
    def __init__(self, data: dict = None):
        if data is not None:
            self._id = data.get("id")
            self._name = data.get("name")
            self._steps = data.get("stepsAmount")
            self._pasteBinLink = data.get("pasteBinLink")
            self._createdAt = data.get("createdAt")
            self._lastUpdatedAt = data.get("lastUpdatedAt")
            self._creator = data.get("creator")
            self._updater = data.get("updater")
            self._VislandRouteItems = data.get("Items", [])
            self._routeCode = data.get("routeCode")
        else:
            self._id = None
            self._name = None
            self._steps = None
            self._pasteBinLink = None
            self._createdAt = None
            self._lastUpdatedAt = None
            self._creatorID = None
            self._updaterID = None
            self._VislandRouteItems = None
            self._routeCode = None

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def steps(self):
        return self._steps
    
    @property
    def pasteBinLink(self):
        return self._pasteBinLink
    
    @property
    def createdAt(self):
        return self._createdAt
    
    @property
    def lastUpdatedAt(self):
        return self._lastUpdatedAt
    
    @property
    def creatorID(self):
        return self._creatorID
    
    @property
    def updaterID(self):
        return self._updaterID
    
    @property
    def VislandRouteItems(self):
        return self._VislandRouteItems
    
    @property
    def routeCode(self):
        return self._routeCode

    @id.setter
    def id(self, value):
        self._id = value

    @name.setter
    def name(self, value):
        self._name = value

    @steps.setter
    def steps(self, value):
        self._steps = value

    @pasteBinLink.setter
    def pasteBinLink(self, value):
        self._pasteBinLink = value

    @createdAt.setter
    def createdAt(self, value):
        self._createAt = value

    @lastUpdatedAt.setter
    def lastUpdatedAt(self, value):
        self._lastUpdatedAt = value

    @creatorID.setter
    def creatorID(self, value):
        self._creatorID = value

    @updaterID.setter
    def updaterID(self, value):
        self._updaterID = value

    @VislandRouteItems.setter
    def VislandRouteItems(self, value):
        self._VislandRouteItems = value

    @routeCode.setter
    def routeCode(self, value):
        self._routeCode = value