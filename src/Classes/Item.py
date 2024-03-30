from marshmallow import Schema, fields

class ItemSchema(Schema):
        id = fields.Int()
        name = fields.Str()
        description = fields.Str()
        isCollectable = fields.Bool()