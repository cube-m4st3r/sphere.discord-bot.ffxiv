class VislandRouteItem:
    def __init__(self, data: dict = None):
        if data is not None:
            self._id = data.get("id")
            self._route = data.get("route")
            self._item = data.get("item")
        else:
            self._id = None
            self._route = None
            self._item = None

    @property
    def id(self):
        return self._id
    
    @property
    def route(self):
        return self._route
    
    @property
    def item(self):
        return self._item
    
    @id.setter
    def id(self, value):
        self._id = value

    @route.setter
    def route(self, value):
        self._route = value

    @item.setter
    def item(self, value):
        self._item, value