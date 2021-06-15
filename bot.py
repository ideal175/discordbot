import discord
from discord.ext import commands


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


client.run('ODU0MDM5NjQ0OTI3Njg4NzYy.YMeIZg.Th82UYM5SPnWdm__d0pLOB0xIQo')
