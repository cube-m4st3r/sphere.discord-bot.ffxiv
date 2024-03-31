from marshmallow import Schema, fields

class PlayableCharacterSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    lodestone_url = fields.Str(required=True)
    world = fields.Str(required=True)