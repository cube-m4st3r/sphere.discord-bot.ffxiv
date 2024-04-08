from marshmallow import Schema, fields
from Schemas.Item import ItemSchema

class VislandRouteItem(Schema):
    id = fields.Int(required=True)
    Item = fields.Nested(ItemSchema)