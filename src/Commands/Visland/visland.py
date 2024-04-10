import discord
from discord import app_commands
from discord.ext import commands
from config import botConfig, config
import aiohttp
from Loaders import load_full_route


class VislandGroup(app_commands.Group):
    @app_commands.command(description="Add a new route.")
    async def add(self, interaction: discord.Interaction, id: int):
        await interaction.response.defer()

    @app_commands.command(description="Search for a specific route.")
    async def search(self, interaction: discord.Interaction, item: str):
        await interaction.response.defer()

        route = await load_full_route(item=item)

        await interaction.followup.send(embed=await build_full_route_embed(route))
                

async def submit_data_to_backend(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{config['backend_url']}/ffxiv/visland/route/add", json=data) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Failed to send data. Status code: {response.status}")
                return None


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
    full_route_embed.add_field(name="Created at:", value=f"{full_route.createdAt["date"]}")
    full_route_embed.add_field(name="Last updated at:", value=f"{full_route.lastUpdatedAt["date"]}")

    return full_route_embed


#class AddRouteModal(discord.ui.Modal):
#    def __init__(self):
#        super().__init__(title="Add a new Route")

class Visland_System(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    visland_system_group = VislandGroup(
        name="visland", description="Visland system related commands.")
    
async def setup(client: commands.Bot) -> None:
    await client.add_cog(Visland_System(client=client), guild=discord.Object(id=botConfig["hub-server-guild-id"]))