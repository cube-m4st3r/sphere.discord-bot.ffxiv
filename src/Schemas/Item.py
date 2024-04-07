from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    isCollectable = fields.Bool(required=True)
    CanBeHQ = fields.Bool(required=True)