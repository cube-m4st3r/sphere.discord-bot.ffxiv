from Classes.Item import Item

class CGOrderItem:
    def __init__(self, amount: int, item: Item):
        self._amount = amount
        self._item = item

    @property
    def amount(self):
        return self._amount

    @property
    def item(self):
        return self._item

    @amount.setter
    def amount(self, value):
        self._amount = value

    @item.setter
    def item(self, value):
        self._item = value
