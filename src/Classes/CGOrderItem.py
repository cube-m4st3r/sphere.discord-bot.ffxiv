from marshmallow import Schema, fields
from Classes.Item import ItemSchema

class CGOrderItemSchema(Schema):
        amount = fields.Int()
        item = fields.Nested(ItemSchema)