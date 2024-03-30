from marshmallow import Schema, fields

class PlayableCharacterSchema(Schema):
        id = fields.Int()
        name = fields.Str()
        last_name = fields.Str()
        lodestone_url = fields.Str()
        world = fields.Str()