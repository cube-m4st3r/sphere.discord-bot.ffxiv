from marshmallow import Schema, fields
from .PlayableCharacter import PlayableCharacterSchema
from .DiscordUser import DiscordUserSchema

class CustomerSchema(Schema):
        id = fields.Int()
        character = fields.Nested(PlayableCharacterSchema)
        discordinfo = fields.Nested(DiscordUserSchema)