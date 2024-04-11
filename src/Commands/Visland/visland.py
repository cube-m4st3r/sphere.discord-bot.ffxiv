import discord
from discord import app_commands
from discord.ext import commands
from config import botConfig, config
import aiohttp
from Loaders import load_full_route
from datetime import datetime
from Classes.DiscordUser import DiscordUser
from Classes.VislandRoute import VislandRoute
from Classes.VislandRouteItem import VislandRouteItem, Item
import json
from Serializers import serialize_visland_route
import datetime


class VislandGroup(app_commands.Group):
    @app_commands.command(description="Add a new route.")
    async def add(self, interaction: discord.Interaction, file: discord.Attachment, name: str):
        #await interaction.response.send_modal(AddRouteModal())

        await handle_visland_info_input(data=await file.read(), interaction=interaction, name=name)

    @app_commands.command(description="Search for a specific route.")
    async def search(self, interaction: discord.Interaction, item: str):
        await interaction.response.defer()

        route = await load_full_route(item=item)

        await interaction.followup.send(embed=await build_full_route_embed(route))
                

async def submit_data_to_backend(data):
    route = await serialize_visland_route(data)
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{config['backend_url']}/ffxiv/visland/route/add", json=route) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Failed to send data. Status code: {response.status}")
                return None


async def handle_visland_info_input(data, interaction, name):
    data_json = json.loads(data)

    route = VislandRoute()
    route.code = str(data)
    route.name = name
    route.steps = len(data_json["Waypoints"])

    current_time = datetime.datetime.now().isoformat()
    route.createdAt = current_time
    route.lastUpdatedAt = current_time

    user = interaction.user
    routeUser = DiscordUser()
    routeUser.id = user.id
    routeUser.username = user.name
    routeUser.avatarUrl = user.avatar.url
    
    route.creator = routeUser
    route.updater = routeUser
    items = data_json["Name"].split("/")
    routeItems = list()
    for itemdata in items:
        item = Item()
        itemdata = itemdata.strip(' ')
        item.name = itemdata
        routeItem = VislandRouteItem(item=item)
        routeItems.append(routeItem)
    
    route.VislandRouteItems = routeItems

    await submit_data_to_backend(data=route)
    


async def build_full_route_embed(full_route):
    formatted_items = ""
    for item_data in full_route.VislandRouteItems:
        formatted_items += f"- {item_data.item.name}\n"

    full_route_embed = discord.Embed()
    full_route_embed.set_thumbnail(url=full_route.creator.avatarUrl)
    full_route_embed.title = f"{full_route.name}"
    full_route_embed.description = f"""**Available Items**:
    {formatted_items}

    **Link to import code**: {full_route.pasteBinLink}"""
    full_route_embed.add_field(name="Steps:", value=f"{full_route.steps}")
    full_route_embed.add_field(name="Creator:", value=f"{full_route.creator.username}")
    full_route_embed.add_field(name="Updater:", value=f"{full_route.updater.username}")

    created_date_str = full_route.createdAt["date"].split('.')[0]
    last_updated_date_str = full_route.lastUpdatedAt["date"].split('.')[0]

    created_date_obj = datetime.datetime.strptime(created_date_str, "%Y-%m-%d %H:%M:%S")
    last_updated_date_obj = datetime.datetime.strptime(last_updated_date_str, "%Y-%m-%d %H:%M:%S")

    full_route_embed.add_field(name="Created at:", value=f"{created_date_obj.strftime('%d.%m.%Y @ %H:%M:%S')}")
    full_route_embed.add_field(name="Last updated at:", value=f"{last_updated_date_obj.strftime('%d.%m.%Y @ %H:%M:%S')}")
    return full_route_embed


class AddRouteModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Add a new Route")

        self.route = VislandRoute(data=None)
        self.routeCreator = DiscordUser(data=None)
        self.routeUpdater = DiscordUser(data=None)

        self.route_name = discord.ui.TextInput(label="Route Name:", style=discord.TextStyle.long,
                                               placeholder="For easier processing, name the route by their items splitted by /", required=True)
        
        self.route_code = discord.ui.TextInput(label="Route Code:", style=discord.TextStyle.long,
                                               placeholder="Insert the route code", required=True)
        
        self.add_item(self.route_name)
        self.add_item(self.route_code)
    
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()

        await handle_visland_info_input(data=self.route_code.value)


class Visland_System(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    visland_system_group = VislandGroup(
        name="visland", description="Visland system related commands.")
    
async def setup(client: commands.Bot) -> None:
    await client.add_cog(Visland_System(client=client), guild=discord.Object(id=botConfig["hub-server-guild-id"]))