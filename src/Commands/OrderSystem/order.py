import discord
from discord import app_commands
from discord.ext import commands
from config import botConfig, config
from Loaders import load_full_cgorder
from Classes.CGOrder import CGOrder
from Classes.Customer import Customer
from Classes.PlayableCharacter import PlayableCharacter
from Classes.DiscordUser import DiscordUser
import aiohttp
from Serializers import serialize_discord_info, serialize_playable_character, serialize_cg_order, serialize_cg_order_item


class OrderGroup(app_commands.Group):
    @app_commands.command(description="View a specified order.")
    async def view(self, interaction: discord.Interaction, id: int):
        await interaction.response.defer()

        full_order = await load_full_cgorder(id=id)

        await interaction.followup.send(embed=await build_full_order_embed(full_order=full_order))

    @app_commands.command(description="Create a new order.")
    async def create(self, interaction: discord.Interaction):
        await interaction.response.send_modal(AddOrderModal())


async def submit_data_to_backend(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{config['backend_url']}/ffxiv/add_gcorder", json=data, ssl=False) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Failed to send data. Status code: {response.status}")
                return None


async def handle_order_info_input(data):
    character = data["character"]
    character.lodestone_url = "" # temp hard code
    character.world = character.world.value

    discord_info = data["discord_info"]
    discord_info.username = discord_info.username.value

    customer = data["customer"]
    customer.character = character
    customer.discord_info = discord_info

    cgOrder = data["cgOrder"]

    if cgOrder.CGOrderItems is not None:
        cg_order_item_data = [await serialize_cg_order_item(item) for item in cgOrder.CGOrderItems]
    else:
        pass

    cgOrder.reward = cgOrder.reward.value
    cgOrder.status = cgOrder.status.value
    cgOrder.CGOrderItems = cg_order_item_data
    cgOrder.customer = customer

    return {**serialize_playable_character(character=character),
            **serialize_discord_info(user=discord_info), 
            "CGOrderItem": cg_order_item_data, 
            **serialize_cg_order(order=cgOrder)}


async def build_full_order_embed(full_order):
    customer = full_order.customer
    character = customer.character
    discord_info = customer.discord_info

    formatted_items = ""
    for item_data in full_order.CGOrderItems:
        formatted_items += f"- {item_data.amount}x {item_data.item.name}\n"

    order_embed = discord.Embed()
    order_embed.title = f"Order ID: #{full_order.id}"
    order_embed.description = f"""**Character Full Name**: {character.name} {character.last_name} @ {character.world}
    **Discord Info**:  {discord_info.username}
    **Items**:
    {formatted_items}"""
    order_embed.add_field(name="Status:", value=f"{full_order.status}")
    order_embed.add_field(name="Reward:", value=f"{full_order.reward} Gil")

    return order_embed


class AddOrderModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title=f"Add a new Order")

        self.cgOrder = CGOrder(data=None)
        self.character = PlayableCharacter(data=None)
        self.discord_info = DiscordUser(data=None)
        self.customer = Customer(data=None)
        self.full_name = str

        self.full_name = discord.ui.TextInput(label="Full Character Name:", style=discord.TextStyle.short,
                                              placeholder="Enter the customer's character name", required=True)

        self.character.world = discord.ui.TextInput(label="Character World:", style=discord.TextStyle.short,
                                                    placeholder="Enter the character's world", required=True)

        #self.character.lodestone_url = discord.ui.TextInput(label="Lodestone URL:", style=discord.TextStyle.short,
                                                            #placeholder="Enter the lodestone url", required=False)

        self.add_item(self.full_name)
        self.add_item(self.character.world)
        #self.add_item(self.character.lodestone_url)

        self.discord_info.username = discord.ui.TextInput(label="Discord Username:", style=discord.TextStyle.short,
                                                          placeholder="Enter the customer's discord username", required=True)

        self.add_item(self.discord_info.username)

        self.cgOrder.reward = discord.ui.TextInput(label="Reward amount:", style=discord.TextStyle.short,
                                                   placeholder="Enter an amount in gil", required=True)

        self.cgOrder.status = discord.ui.TextInput(label="Order Status:", style=discord.TextStyle.short,
                                                   placeholder="WIP, DONE, ON HOLD", required=True)

        self.add_item(self.cgOrder.reward)
        self.add_item(self.cgOrder.status)

    async def on_submit(self, interaction: discord.Interaction):
        interaction.response.defer()

        self.character._split_full_name(full_name=self.full_name.value)

        data = await handle_order_info_input(data={
            "character": self.character,
            "discord_info": self.discord_info,
            "customer": self.customer,
            "cgOrder": self.cgOrder
        })

        response_json = await submit_data_to_backend(data=data)
        if response_json:
            full_order = await load_full_cgorder(id=response_json["id"])

            await interaction.response.send_message(embed=await build_full_order_embed(full_order=full_order))

        else:
            await interaction.response.send_message(content="An error occured.")


class Order_System(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    order_system_group = OrderGroup(
        name="order", description="Order system related commands.")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Order_System(client=client), guild=discord.Object(id=botConfig["hub-server-guild-id"]))
