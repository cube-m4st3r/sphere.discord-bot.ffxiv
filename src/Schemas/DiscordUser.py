from marshmallow import Schema, fields

class DiscordUserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
