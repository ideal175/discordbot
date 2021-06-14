import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready(ctx):
    await ctx.send("ideal made this bot now sub !yt")

@client.event
async def on_ready():
    print("bot ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hello Drke Drke Dzon")

@client.command()
async def h(ctx):
    await ctx.send("hello Im Drke Drke John theese are all commands right now I hope i helped you :),!hello,!whatyouknow,!plsjoke,!yt")

@client.command()
async def whatyouknow(ctx):
    await ctx.send("BOUT ROLLING DOWN IN THE DEEP!  :rofl: ")

@client.command()
async def plsjoke(ctx):
    await ctx.send("9/11,sorry i had to  :rofl: ")

@client.command()
async def yt(ctx):
    await ctx.send("https://www.youtube.com/channel/UCLN1vLtK5SU1saRlo1pwCLA")


client.run('ODU0MDM5NjQ0OTI3Njg4NzYy.YMeIZg.8StXfHr0R5IQ0CCEmQqn2bRXMC0')
