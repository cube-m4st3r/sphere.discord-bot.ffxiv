from Schemas.CGOrder import CGOrderSchema, CGOrderItemSchema
from Schemas.Customer import CustomerSchema, PlayableCharacterSchema, DiscordUserSchema
from Schemas.Item import ItemSchema


def deserialize_playable_character(data: dict):
    playable_character = PlayableCharacterSchema()
    return playable_character.load(data=data)


def deserialize_discord_user(data: dict):
    discord_user_schema = DiscordUserSchema()
    return discord_user_schema.load(data)


def deserialize_customer(data: dict, character: PlayableCharacterSchema, discord_info: DiscordUserSchema):
    customer_schema = CustomerSchema()
    return customer_schema.load({
        "id": data["customer_id"],
        "character": character,
        "discord_info": discord_info  # Corrected key from "discordinfo" to "discord_info"
    })


def deserialize_item(data: dict):
    item_schema = ItemSchema()
    return item_schema.load(data)


def deserialize_cgOrder_item(item: ItemSchema, amount: int):
    cgOrder_item_schema = CGOrderItemSchema()
    return cgOrder_item_schema.load({
        "item": item,
        "amount": amount
    })


def deserialize_cgOrder(data: dict, customer: CustomerSchema, items: list):
    cgOrder_schema = CGOrderSchema()
    return cgOrder_schema.load({
        "id": data["id"],
        "customer": customer,
        "status": data["status"],
        "reward": data["reward"],
        "CGOrderItems": items
    })


def serialize_playable_character(character):
    return {
        "PlayableCharacter": {
            "name": character.name,
            "last_name": character.last_name,
            "world": character.world,
            "lodestone_url": character.lodestone_url
        }
    }


def serialize_discord_info(user):
    return {
        "DiscordUser": {
            "username": user.username
        }
    }


def serialize_item(item):
    return {
        "id": item.id,
        "name": item.name,
        "description": item.description,
        "isCollectable": item.isCollectable,
        "canBeHQ": item.isCanBeHQ
    }


def serialize_cg_order_item(item):
    return {
        "amount": item.amount,
        "Item": serialize_item(item.item)
    }


def serialize_cg_order(order):
    cg_order_items = [serialize_cg_order_item(
        item) for item in order.CGOrderItems]
    return {
        "CGOrderItem": cg_order_items,
        "CGOrder": {
            "status": order.status,
            "reward": order.reward
        }
    }
