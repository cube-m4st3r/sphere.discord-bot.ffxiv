from Schemas.CGOrder import CGOrderSchema, CGOrderItemSchema
from Schemas.Customer import CustomerSchema, PlayableCharacterSchema, DiscordUserSchema
from Schemas.Item import ItemSchema
from Schemas.VislandRoute import VislandRouteSchema, VislandRouteItemSchema


async def deserialize_playable_character(data: dict):
    playable_character = PlayableCharacterSchema()
    return playable_character.load(data=data)


async def deserialize_discord_user(data: dict):
    discord_user_schema = DiscordUserSchema()
    return discord_user_schema.load(data)


async def deserialize_customer(data: dict, character: PlayableCharacterSchema, discord_info: DiscordUserSchema):
    customer_schema = CustomerSchema()
    return customer_schema.load({
        "id": data["customer_id"],
        "character": character,
        "discord_info": discord_info 
    })


async def deserialize_item(data: dict):
    item_schema = ItemSchema()
    return item_schema.load(data)


async def deserialize_cgOrder_item(item: ItemSchema, amount: int):
    cgOrder_item_schema = CGOrderItemSchema()
    return cgOrder_item_schema.load({
        "item": item,
        "amount": amount
    })


async def deserialize_cgOrder(data: dict, customer: CustomerSchema, items: list):
    cgOrder_schema = CGOrderSchema()
    return cgOrder_schema.load({
        "id": data["id"],
        "customer": customer,
        "status": data["status"],
        "reward": data["reward"],
        "CGOrderItems": items
    })

async def deserialize_vislandRouteItem(item: ItemSchema):
    vislandRouteItem_schema = VislandRouteItemSchema()
    return vislandRouteItem_schema.load({
        "item": item
    })

async def deserialize_vislandRoute(data: dict, creator: DiscordUserSchema, updater: DiscordUserSchema, items: list):
    vislandRoute_schema = VislandRouteSchema()
    return vislandRoute_schema.load({
        "id": data["id"],
        "name": data["name"],
        "steps": data["steps"],
        "pasteBinLink": data["pasteBinLink"],
        "created_at": data["createdAt"]["date"],
        "lastUpdated_at": data["lastUpdatedAt"]["date"],
        "creator": creator,
        "updater": updater,
        "code": data["code"],
        "vislandrouteitem": items
    })
