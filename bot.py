import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("DrkeDrkeDzon is Online")

@client.command()
async def hello(ctx):
    await ctx.send("Hello Kidaro")

@client.command()
async def h(ctx):
    await ctx.send("!hello,!whatyouknow,!plsjoke,!yt")

@client.command()
async def whatyouknow(ctx):
    await ctx.send("BOUT ROLLING DOWN IN THE DEEP!  :rofl: ")

@client.command()
async def plsjoke(ctx):
    await ctx.send("9/11  :rofl: ")

@client.command()
async def yt(ctx):
    await ctx.send("https://www.youtube.com/channel/UCLN1vLtK5SU1saRlo1pwCLA")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("you need to be in voice channel to make bot join")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice-client.disconnect()
        await ctx.send("I Left the voice channel")
    else:
        await ctx.send("Im not in voice channel")

client.run(os.getenv('TOKEN'))
