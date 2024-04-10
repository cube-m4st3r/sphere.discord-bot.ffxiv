from Schemas.CGOrder import CGOrderSchema, CGOrderItemSchema
from Schemas.Customer import CustomerSchema, PlayableCharacterSchema, DiscordUserSchema
from Schemas.Item import ItemSchema


async def serialize_playable_character(character):
    return PlayableCharacterSchema.dump(character)


async def serialize_discord_info(user):
    return DiscordUserSchema.dump(user)


async def serialize_item(item):
    return ItemSchema.dump(item)


async def serialize_cg_order_item(item):
    return CGOrderItemSchema.dump(item)


async def serialize_cg_order(order):
    return CGOrderSchema.dump(order)
