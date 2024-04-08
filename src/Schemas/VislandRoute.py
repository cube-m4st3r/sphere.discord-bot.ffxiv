from marshmallow import Schema, fields
from Schemas.DiscordUser import DiscordUserSchema
from Schemas.VislandRouteItem import VislandRouteItemSchema

class VislandRouteSchema(Schema):
    id = fields.Int(required=True)
    name = fields.String(required=True)
    steps = fields.Int(required=True)
    pastebinlink = fields.String(required=True)
    created_at = fields.DateTime(required=True)
    last_updated_at = fields.DateTime(required=True)
    creator = fields.Nested(DiscordUserSchema)
    updater = fields.Nested(DiscordUserSchema)
    vislandrouteitem = fields.List(fields.Nested(VislandRouteItemSchema))
    routeCode = fields.String(required=True)
