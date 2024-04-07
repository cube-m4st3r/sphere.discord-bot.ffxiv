import discord
from discord import app_commands
from discord.ext import commands
from config import botConfig, config


class CharacterGroup(app_commands.Group):
    @app_commands.command(description="Inspect your character.")
    async def inspect(self, interaction: discord.Interaction):
        await interaction.response.defer() 