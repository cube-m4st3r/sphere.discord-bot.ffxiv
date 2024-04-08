from config import config
import aiohttp
from Serializers import deserialize_playable_character, deserialize_discord_user, deserialize_customer, deserialize_item, deserialize_cgOrder_item, deserialize_cgOrder
from Classes.PlayableCharacter import PlayableCharacter
from Classes.DiscordUser import DiscordUser
from Classes.Customer import Customer
from Classes.CGOrderItem import Item
from Classes.CGOrder import CGOrder, CGOrderItem

async def load_playable_character(data: dict):
    return PlayableCharacter(data=data)

async def load_discord_info(data: dict):
    return DiscordUser(data=data)

async def load_customer(data: dict):
    return Customer(data=data)

async def load_item(data: dict):
    return Item(data=data)

async def load_cgOrder_item(amount: int, item: Item):
    return CGOrderItem(
        amount=amount,
        item=item
    )

async def load_cgOrder(data, customer: Customer, cgOrder_items: list):
    data["customer"] = customer
    data["CGOrderItems"] = cgOrder_items
    return CGOrder(data=data)

async def load_full_cgorder(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{config["backend_url"]}/ffxiv/get_cgorder/{id}', verify_ssl=False) as response:
            data = await response.json()

            # serialize PlayableCharacter
            playable_character_serialized = await deserialize_playable_character(data=data["PlayableCharacter"])

            # serialize DiscordUser
            discord_info_serialized = await deserialize_discord_user(data=data["DiscordUser"])

            # Load Customer
            loaded_customer = await load_customer(data={**data, **playable_character_serialized, **discord_info_serialized})

            # Load CGOrderItems
            items = []
            for item in data["CGOrderItem"]:
                item_serialized = await deserialize_item(data=item["Item"])
                loaded_item = await load_item(item_serialized)
                loaded_cg_order_item = await load_cgOrder_item(amount=item["amount"], item=loaded_item)
                items.append(loaded_cg_order_item)

            # Load CGOrder
            loaded_cgOrder = await load_cgOrder(data=data["CGOrder"], customer=loaded_customer, cgOrder_items=items)

            return loaded_cgOrder

#load_full_cgorder(1)