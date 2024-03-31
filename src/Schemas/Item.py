from marshmallow import Schema, fields, post_load
from Classes.Item import Item

class ItemSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    isCollectable = fields.Bool(required=True)