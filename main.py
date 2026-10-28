import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="=", case_insensitive=True, intents=intents)


@bot.command()
async def play(ctx, *, content: str):
    if ctx.author.voice:
        channel =  ctx.author.voice.channel

        await channel.connect()
        await ctx.send(f"Joined {channel.name}!")
    else:
        await ctx.send("You must be in a voice channel first!");

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected from the voice channel.")
    else:
        await ctx.send("I am not connected to any voice channel.")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


if __name__ == "__main__":
    bot.run(TOKEN)