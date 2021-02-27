import discord
import tweepy
import requests


from discord.ext import commands

##twitter api 
consumer_key ="Your consummer_key" 
consumer_secret = "Your consumer_secret"
access_token = "Your access_token"
access_token_secret = "Your access_token_secret"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)



api = tweepy.API(auth)




client = commands.Bot(command_prefix = '^')


@client.event
async def on_ready():
    print("BOT READY")
#twitter trend
@client.command()
async def trend(Botrespond):
    world = 1225448 #THAILAND            
    trends = api.trends_place(world)
    
    for value in trends: 
      
        for trend in value['trends'][:5]: 
            
            await (Botrespond.send)(trend['name'])
client.run("Your client discord")
