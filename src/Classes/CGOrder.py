from Classes.Customer import Customer
from Classes.CGOrderItem import CGOrderItem

class CGOrder:
    def __init__(self, data: dict = None):
        if data is not None:
            self._id = data.get("id")
            self._customer = data.get("customer")
            self._status = data.get("status")
            self._reward = data.get("reward")
            self._CGOrderItems = data.get("CGOrderItems", [])
        else:
            self._id = None
            self._customer = None
            self._status = None
            self._reward = None
            self._CGOrderItems = []

    @property
    def id(self):
        return self._id

    @property
    def customer(self):
        return self._customer

    @property
    def status(self):
        return self._status

    @property
    def reward(self):
        return self._reward

    @property
    def CGOrderItems(self):
        return self._CGOrderItems

    @id.setter
    def id(self, value):
        self._id = value

    @customer.setter
    def customer(self, value):
        self._customer = value

    @status.setter
    def status(self, value):
        self._status = value

    @reward.setter
    def reward(self, value):
        self._reward = value

    @CGOrderItems.setter
    def CGOrderItems(self, value):
        self._CGOrderItems = value
