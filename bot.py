# coding: utf-8

import discord

bot = discord.Client()

# Source of messages
channel_source_id = 648827772151660554 #faq_m1_aka_zoomers 

# Target for messages
channel_destination_id = 648849213177987094 #autre-serveur 

bot_id = None


@bot.event
async def on_ready():
    global bot_id
    
    app_info = await bot.application_info()
    bot_id = app_info.id

    print("Ready! bot invite:\n https://discordapp.com/api/oauth2/authorize?client_id=" +
        str(bot_id) + "&permissions=0&scope=bot")


@bot.event
async def on_message(message):

    # Si ce n'est pas le bot qui parle ET que c'est le bon channel
    if( bot_id != message.author.id and message.channel.id == channel_source_id):
        message_content = message.content
        #print(message.author, message_content)
        
        embed = discord.Embed(title=str(message.author), description=message_content, color=0x00ff00)
        channel = bot.get_channel(channel_source_id)
        await channel.send(embed=embed)
    pass


# The token of the bot is stored inside a file
token = open("token").read().rstrip()
bot.run(token)