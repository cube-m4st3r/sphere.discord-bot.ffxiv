from marshmallow import Schema, fields
from Schemas.PlayableCharacter import PlayableCharacterSchema
from Schemas.DiscordUser import DiscordUserSchema

class CustomerSchema(Schema):
    id = fields.Int()
    character = fields.Nested(PlayableCharacterSchema)
    discord_info = fields.Nested(DiscordUserSchema)