from marshmallow import Schema, fields
from Classes.Customer import CustomerSchema
from Classes.CGOrderItem import CGOrderItemSchema

class CGOrderSchema(Schema):
        id = fields.Int()
        customer = fields.Nested(CustomerSchema)
        status = fields.Str()
        reward = fields.Int()
        CGOrderItems = fields.List(fields.Nested(CGOrderItemSchema))