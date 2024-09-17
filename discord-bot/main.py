import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from responses import get_ranked_stats_response

# Load environment variables from the .env file
load_dotenv()

# Retrieve Discord token and API key
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
VAL_API_KEY = os.getenv("VAL_API_KEY")

# Bot setup
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='/', intents=intents)


# Command to fetch ranked stats
@bot.command(name="rankedstats")
async def stats(ctx, region: str, platform: str, *, name_tag: str):
    """
    Fetches ranked stats for a Valorant account.
    Usage: /rankedstats <region> <platform> <name>#<tag>
    Example: /rankedstats na pc chris#1234
    """
    try:
        # Split the name and tag by '#' - this allows users to have spaces in their names
        if '#' not in name_tag:
            await ctx.send("Error: Please provide the name and tag in the format 'name#tag'.")
            return

        name, tag = name_tag.rsplit('#', 1)  # Split into name and tag

        # fetch ranked stats using get_ranked_stats_response function
        response = get_ranked_stats_response(region, platform, name, tag, VAL_API_KEY)
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {e}")


# run bot using discord token
bot.run(DISCORD_TOKEN)
