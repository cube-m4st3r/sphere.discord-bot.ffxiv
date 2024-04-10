from Classes.Item import Item

class VislandRouteItem:
    def __init__(self, item: Item = None):
        if item is not None:
            self._item = item
        else:
            self._item = None

    @property
    def id(self):
        return self._id
    
    @property
    def item(self):
        return self._item
    
    @id.setter
    def id(self, value):
        self._id = value

    @item.setter
    def item(self, value):
        self._item, value