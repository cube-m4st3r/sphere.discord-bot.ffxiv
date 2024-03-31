from marshmallow import Schema, fields
from Schemas.Customer import CustomerSchema
from Schemas.CGOrderItem import CGOrderItemSchema

class CGOrderSchema(Schema):
    id = fields.Int(required=True)
    customer = fields.Nested(CustomerSchema)
    status = fields.Str(required=True)
    reward = fields.Int(required=True)
    CGOrderItems = fields.List(fields.Nested(CGOrderItemSchema))
