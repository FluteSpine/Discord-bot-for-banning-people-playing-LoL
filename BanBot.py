
import discord
import datetime
from discord.ext import commands, tasks

intents = discord.Intents().all() #sadge

with open('token.txt') as file:
    token = file.readline()

intents.members = True
intents.messages = True
intents.presences = True

bot = commands.Bot(command_prefix="?", intents = discord.Intents().all())

@bot.event
async def on_ready():
    CheckGameDuration.start()
    print("Discord bot ready")

@discord.ext.tasks.loop(seconds = 60)
async def CheckGameDuration():
    for guild in bot.guilds:
        for member in guild.members:
            if member.activity is not None and member.bot != True:
                if member.activity.type == discord.ActivityType.playing:
                    if str(member.activity.name).lower() == 'league of legends':
                        deltaMinutes = "{:.0f}".format((datetime.datetime.utcnow() - member.activity.created_at).total_seconds() / 60)
                        if int(deltaMinutes) > 30:
                            #print(f'{member.name} been playing {member.activity.name} for {deltaMinutes} minutes')
                            await guild.kick(member, reason = f'Stop playing so much {member.activity.name}')

bot.run(token)
