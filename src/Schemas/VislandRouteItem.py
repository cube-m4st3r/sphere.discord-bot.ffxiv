from marshmallow import Schema, fields
from Schemas.Item import ItemSchema

class VislandRouteItemSchema(Schema):
    id = fields.Int(required=True)
    Item = fields.Nested(ItemSchema)