import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

input_channel_ID = 1274385334364405795
bot = commands.Bot(command_prefix="!", intents=intents)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Define the channels according to emojis
emoji_channels = {
    '📕' : 1274442500538634240, #todo
    '📗' : 1274442633841868931, #thoughts
    '📘' : 1274442718768136222, #experiences
    '📙' : 1274442750300913798 #amusing
    #etc
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.channel.id == input_channel_ID:
        emojis = ['📕','📗', '📘', '📙']
        for emoji in emojis:
            await message.add_reaction(emoji)
    await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if reaction.message.channel.id == input_channel_ID:
        emoji = reaction.emoji
        if emoji in emoji_channels:
            target_channel_id = emoji_channels[emoji]
            target_channel = bot.get_channel(target_channel_id)
            if target_channel:
                await target_channel.send(reaction.message.content)

#Now for the best part:
bot.run(TOKEN)

