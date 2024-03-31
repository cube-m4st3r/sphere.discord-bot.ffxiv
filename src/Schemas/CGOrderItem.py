from marshmallow import Schema, fields
from Schemas.Item import ItemSchema

class CGOrderItemSchema(Schema):
    amount = fields.Int(required=True)
    item = fields.Nested(ItemSchema)
