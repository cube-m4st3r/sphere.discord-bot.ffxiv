from config import config
import requests
from Serializers import deserialize_playable_character, deserialize_discord_user, deserialize_customer, deserialize_item, deserialize_cgOrder_item, deserialize_cgOrder
from Classes.PlayableCharacter import PlayableCharacter
from Classes.DiscordUser import DiscordUser
from Classes.Customer import Customer
from Classes.CGOrderItem import Item
from Classes.CGOrder import CGOrder, CGOrderItem

def load_playable_character(data: dict):
    return PlayableCharacter(data=data)

def load_discord_info(data: dict):
    return DiscordUser(data=data)

def load_customer(data: dict):
    return Customer(data=data)

def load_item(data: dict):
    return Item(data=data)

def load_cgOrder_item(amount: int, item: Item):
    return CGOrderItem(
        amount=amount,
        item=item
    )

def load_cgOrder(data, customer: Customer, cgOrder_items: list):
    data["customer"] = customer
    data["CGOrderItems"] = cgOrder_items
    return CGOrder(data=data)

def load_full_cgorder(id): # BASE LOADER FOR A FULL ORDER
    response = requests.get(f'{config["backend_url"]}/ffxiv/get_cgorder/{id}', verify=False)
    data = response.json()

    # serialize PlayableCharacter
    playable_character_serialized = deserialize_playable_character(data=data["PlayableCharacter"])

    # load PlayableCharacter
    #playable_character = load_playable_character(data=playable_character_serialized)

    # serialize DiscordUser
    discord_info_serialized = deserialize_discord_user(data=data["DiscordUser"])

    #loaded_discord_info = load_discord_info(data=discord_info_serialized)

    # Load Customer
    #customer_serialized = deserialize_customer(data=data["CGOrder"], character=playable_character_serialized,
                                             #discord_info=discord_info_serialized) 

    loaded_customer = load_customer(data={**data, **playable_character_serialized, **discord_info_serialized})

    # Load CGOrderItems
    items = []
    for item in data["CGOrderItem"]:
        item_serialized = deserialize_item(data=item["Item"])
        loaded_item = load_item(item_serialized)
        #cg_order_item_serialized = deserialize_cgOrder_item(item=item_serialized, amount=item["amount"])
        loaded_cg_order_item = load_cgOrder_item(amount=item["amount"], item=loaded_item)
        items.append(loaded_cg_order_item)

    # Load CGOrder
    # cgOrder_serialized = serialize_cgOrder(data=data["CGOrder"], customer=customer_serialized, items=items)

    loaded_cgOrder = load_cgOrder(data=data["CGOrder"], customer=loaded_customer, cgOrder_items=items)

    #print(loaded_cgOrder.CGOrderItems)
    #print(loaded_cgOrder.customer.character.name)

    return loaded_cgOrder

#load_full_cgorder(1)