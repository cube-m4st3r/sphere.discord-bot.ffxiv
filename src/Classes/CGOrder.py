from Classes.Customer import Customer
from Classes.CGOrderItem import CGOrderItem

class CGOrder:
    def __init__(self, id: int, customer: Customer, status: str, reward: int, CGOrderItems: list):
        self._id = id
        self._customer = customer
        self._status = status
        self._reward = reward
        self._CGOrderItems = CGOrderItems

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
