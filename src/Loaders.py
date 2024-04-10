from config import config
import aiohttp
from Deserializers import deserialize_playable_character, deserialize_discord_user, deserialize_item
from Classes.PlayableCharacter import PlayableCharacter
from Classes.DiscordUser import DiscordUser
from Classes.Customer import Customer
from Classes.CGOrderItem import CGOrderItem, Item
from Classes.CGOrder import CGOrder
from Classes.VislandRoute import VislandRoute
from Classes.VislandRouteItem import VislandRouteItem

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

async def load_vislandroute_item(item: Item):
    return VislandRouteItem(item=item)

async def load_vislandroute(data: dict, route_items: list):
    data["VislandRouteItems"] = route_items
    data["creator"] = await load_discord_info(data=data["creator"])
    data["updater"] = await load_discord_info(data=data["updater"])
    return VislandRoute(data=data)

async def load_full_cgorder(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{config["backend_url"]}/ffxiv/get_cgorder/{id}', verify_ssl=False) as response:
            data = await response.json()

            playable_character_deserialized = await deserialize_playable_character(data=data["PlayableCharacter"])

            discord_info_deserialized = await deserialize_discord_user(data=data["DiscordUser"])

            loaded_customer = await load_customer(data={**data, **playable_character_deserialized, **discord_info_deserialized})

            items = []
            for item in data["CGOrderItem"]:
                item_serialized = await deserialize_item(data=item["Item"])
                loaded_item = await load_item(item_serialized)
                loaded_cg_order_item = await load_cgOrder_item(amount=item["amount"], item=loaded_item)
                items.append(loaded_cg_order_item)

            loaded_cgOrder = await load_cgOrder(data=data["CGOrder"], customer=loaded_customer, cgOrder_items=items)

            return loaded_cgOrder


async def load_full_route(item):
    async with aiohttp.ClientSession() as session:
            async with session.get(f"{config['backend_url']}/ffxiv/visland/route/search", params={'item_name': item}, verify_ssl=False) as response:
                if response.status == 200:
                    data = await response.json()

                    route_items = []
                    for item_data in data["VislandRouteItems"]:
                        route_item = await load_vislandroute_item(await load_item(data=item_data["Item"]))
                        route_items.append(route_item)

                    route = await load_vislandroute(data=data, route_items=route_items)
                    return route
                else:
                    print(f"Failed to fetch data. Status code: {response.status}")
                    return None