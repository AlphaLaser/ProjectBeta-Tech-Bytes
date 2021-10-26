# Imports
import os
import discord
import time 
import requests
from newsapi.newsapi_client import NewsApiClient
import random
import threading


# Defining Start Time so that the bot can send messages every hour
starttime = time.time()


# Defining the key for the news API through environment variables
newsapi = NewsApiClient(api_key=os.getenv('newsAPI-Key'))


#Creating an instance of the Discord Client Class
bot = discord.Client()


# Topic list for a random news headline related to these topics
topics = ['technology','business']


# Getting the bot onlline
@bot.event
async def on_ready():
	print("Ready to Use")

# NewsApi
@bot.event
async def on_message(message) :
	if message.author == bot.user : 
		return

	

	if message.content.startswith('-n'):

		query = random.choice(topics)

		if query == 'technology' :
			await message.channel.send("**Topic :** Technology ")

		elif query == 'business' :
			await message.channel.send("**Topic :** Entrpreneurship / Business")
		top_headlines = newsapi.get_top_headlines(category=query,language='en')
		
		articles = (top_headlines['articles'] )
		article_len = len(articles)
		final_len = (article_len-1)
		x = (random.randint(0, final_len))
		await message.channel.send((top_headlines['articles'])[x]['url'])


bot.run(os.getenv('TOKEN'))

