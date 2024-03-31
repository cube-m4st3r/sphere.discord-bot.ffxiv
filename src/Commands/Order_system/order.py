import discord
from discord import app_commands
from discord.ext import commands
from config import botConfig
from Loaders import load_full_cgorder


class OrderGroup(app_commands.Group):
    @app_commands.command(description="View a specified order.")
    async def view(self, interaction: discord.Interaction, id: int):
        await interaction.response.defer()

        full_order = load_full_cgorder(id=id)
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

        await interaction.followup.send(embed=order_embed)

class Order_System(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    order_system_group = OrderGroup(name="order", description="Order system related commands.")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Order_System(client=client), guild=discord.Object(id=botConfig["hub-server-guild-id"]))