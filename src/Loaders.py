from config import config
import requests
from Serializers import serialize_playable_character, serialize_discord_user, serialize_customer, serialize_item, serialize_cgOrder_item, serialize_cgOrder
from Classes.PlayableCharacter import PlayableCharacter
from Classes.DiscordUser import DiscordUser
from Classes.Customer import Customer
from Classes.CGOrderItem import Item
from Classes.CGOrder import CGOrder, CGOrderItem

def load_playable_character(data: dict):
    return PlayableCharacter(
        id=data["id"],
        name=data["name"],
        last_name=data["last_name"],
        lodestone_url=data["lodestone_url"],
        world=data["world"]
    )

def load_discord_info(data: dict):
    return DiscordUser(
        id=data["id"],
        username=data["username"]
    )

def load_customer(data: dict, character: PlayableCharacter, discord_info: DiscordUser):
    return Customer(
        id=data["id"],
        character=character,
        discord_info=discord_info
    )

def load_item(data: dict):
    return Item(
        id=data["id"],
        name=data["name"],
        description=data["description"],
        isCollectable=data["isCollectable"]
    )

def load_cgOrder_item(amount: int, item: Item):
    return CGOrderItem(
        amount=amount,
        item=item
    )

def load_cgOrder(data, customer: Customer, cgOrder_items: list):
    return CGOrder(
        id=data["id"],
        customer=customer,
        status=data["status"],
        reward=data["reward"],
        CGOrderItems=cgOrder_items
    )

def load_full_cgorder(id): # BASE LOADER FOR A FULL ORDER
    response = requests.get(f'{config["backend_url"]}/ffxiv/get_cgorder/{id}', verify=False)
    data = response.json()

    # serialize PlayableCharacter
    playable_character_serialized = serialize_playable_character(data=data["PlayableCharacter"])

    # load PlayableCharacter
    playable_character = load_playable_character(data=playable_character_serialized)

    # serialize DiscordUser
    discord_info_serialized = serialize_discord_user(data=data["DiscordUser"])

    loaded_discord_info = load_discord_info(data=discord_info_serialized)

    # Load Customer
    customer_serialized = serialize_customer(data=data["CGOrder"], character=playable_character_serialized,
                                             discord_info=discord_info_serialized) 
    
    loaded_customer = load_customer(data=customer_serialized, character=playable_character, discord_info=loaded_discord_info)

    # Load CGOrderItems
    items = []
    for item in data["CGOrderItem"]:
        item_serialized = serialize_item(data=item["Item"])
        loaded_item = load_item(item_serialized)
        cg_order_item_serialized = serialize_cgOrder_item(item=item_serialized, amount=item["amount"])
        loaded_cg_order_item = load_cgOrder_item(amount=item["amount"], item=loaded_item)
        items.append(loaded_cg_order_item)

    # Load CGOrder
    # cgOrder_serialized = serialize_cgOrder(data=data["CGOrder"], customer=customer_serialized, items=items)

    loaded_cgOrder = load_cgOrder(data=data["CGOrder"], customer=loaded_customer, cgOrder_items=items)

    return loaded_cgOrder

#load_full_cgorder(7)