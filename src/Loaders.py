from config import config
import requests
from Classes.CGOrder import CGOrderSchema, CGOrderItemSchema
from Classes.Customer import CustomerSchema, PlayableCharacterSchema, DiscordUserSchema
from Classes.Item import ItemSchema

def load_full_cgorder(): # BASE LOADER FOR A FULL ORDER
    response = requests.get(f'{config["backend_url"]}/ffxiv/get_cgorder/4', verify=False)
    data = response.json()

    character_schema = PlayableCharacterSchema()
    playable_character = character_schema.load(data["PlayableCharacter"])

    discord_info_schema = DiscordUserSchema()
    discord_info = discord_info_schema.load(data["DiscordUser"])

    customer_schema = CustomerSchema()
    loaded_customer = customer_schema.load({
        "id": data["CGOrder"]["customer_id"],
        "character": playable_character,
        "discordinfo": discord_info
    })

    items = []
    for item in data["CGOrderItem"]:
        item_schema = ItemSchema()
        loaded_item = item_schema.load(item["Item"])
        cg_order_item_schema = CGOrderItemSchema()
        cg_order_item = cg_order_item_schema.load({
            "item": loaded_item,
            "amount": item["amount"]
        })
        items.append(cg_order_item)

    cg_order_schema = CGOrderSchema()
    loaded_cg_order = cg_order_schema.load({
        "id": data["CGOrder"]["id"],
        "customer": loaded_customer, 
        "status": data["CGOrder"]["status"],
        "reward": data["CGOrder"]["reward"],
        "CGOrderItems": items
    })
    
    return loaded_cg_order

load_full_cgorder()