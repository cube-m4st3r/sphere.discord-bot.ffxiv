from Schemas.CGOrder import CGOrderSchema, CGOrderItemSchema
from Schemas.Customer import PlayableCharacterSchema, DiscordUserSchema
from Schemas.Item import ItemSchema
from Schemas.VislandRoute import VislandRouteSchema
import json


async def serialize_playable_character(character):
    return PlayableCharacterSchema.dump(character)


async def serialize_discord_info(user):
    schema = DiscordUserSchema()
    return schema.dump(obj=user)


async def serialize_item(item):
    return ItemSchema.dump(item)


async def serialize_cg_order_item(item):
    return CGOrderItemSchema.dump(item)


async def serialize_cg_order(order):
    return CGOrderSchema.dump(order)

async def serialize_visland_route(route):
    vislandroute = dict({
        'name': route.name,
        'steps': route.steps,
        'createdAt': route.createdAt,
        'lastUpdatedAt': route.lastUpdatedAt,
        'creator': await serialize_discord_info(route.creator),
        'updater': await serialize_discord_info(route.updater),
        'code': route.code,
        'VislandRouteItems': []
    })

    for routeItem in route.VislandRouteItems:
        item = routeItem.item
        vislandroute['VislandRouteItems'].append({
            'Item': {
                'name': item.name
            } 
        })

    return vislandroute
        
