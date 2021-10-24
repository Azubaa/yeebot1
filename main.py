import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot du BG")

@bot.event
async def on_ready():
    print("Bot Opérationnel !")

#### PERSONELLE ###

#Quand on dit !classe ça répond Les 3ème2 sont les meilleurs !
@bot.command()
async def classe(ctx):
    await ctx.send("Les 3ème2 sont les meilleurs !")

#Quand on dit !evan ça répond Evan a le plus grand Bangala !!
@bot.command()
async def evan(ctx):
	await ctx.send("Evan a le plus grand Bangala !!")

#Quand on dit !chloe ça répond Chloé est la plus forte en Allemand en Anglais !
@bot.command()
async def chloe(ctx):
    await ctx.send("Chloé est la plus forte en Allemand et Anglais !")

### COMMANDES ###

#Quand on dit !serveurstat ça répond les informations
@bot.command()
async def serveurstat(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
	await ctx.send(message)

### TOKEN ###

bot.run("ODk4OTEyNzk4MjE2NjkxNzUz.YWrHyA.BRh65-gGdluAJxNNAhu0CofYZQw")