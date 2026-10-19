import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="=", case_insensitive=True, intents=intents)


@bot.command()
async def play(ctx, *, content: str):
    await ctx.send("I can play " + content)


if __name__ == "__main__":
    bot.run(TOKEN)