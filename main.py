from pathlib import Path
import discord
from discord import app_commands

# Read bot token from "token.txt" in the same folder as "main.py"
token_path = Path(__file__).with_name("token.txt")
with token_path.open("r") as token_file:
    bot_token = token_file.read()

intents = discord.Intents.none() # bot only uses slash commands, no intents needed

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    # await tree.sync() # ONLY UNCOMMENT ONCE WHEN YOU RUN THE BOT FOR THE FIRST TIME

client.run(bot_token)