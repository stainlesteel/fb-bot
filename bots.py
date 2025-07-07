import os
import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option


tool = ('get your own discord api')

bot = commands.Bot()


@bot.slash_command(
    name="fb",
    description="sends fb."
)

async def fb(ctx: discord.ApplicationContext, number: int = Option(int, description="Enter number of output times.", min_value=1)):
     outppot = "fb\n" * number
     await ctx.respond(outppot) 

  

bot.run(tool)




 
