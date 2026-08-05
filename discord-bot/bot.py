import os
import discord
import requests
import random
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('SERVERID')

intents = discord.Intents.default()  

client = discord.Client(intents=intents)
intents.message_content = True

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "hello" or message.content.lower() == "hi":
        username = str(message.author).split("#")[0]
        await message.channel.send(f'Hello {username}!')
        return
    elif message.content.lower() == "bye":
        await message.channel.send(f'Have a nice day')
        return
    elif message.content == "!quote":
        response = requests.get("https://dummyjson.com/quotes").json()
        index = random.randint(1,30)
        quotes = response["quotes"]
        quote = quotes[index-1]
        await message.channel.send(quote["quote"])
        return
    elif message.content == "!challenge" or message.content == "!list" or message.content.startswith("!add"):
        with open('challenges.json', 'r') as file:
            data = json.load(file)

        challenges_str = json.dumps(data, indent=4)
        challenges_dict = json.loads(challenges_str)
        challenges = challenges_dict["challenges"]
        if message.content == "!challenge":
            index = random.randint(0,len(challenges)-1)
            challenge = challenges[index]
            reply = f"{challenge["name"]}: {challenge["url"]}"
            await message.channel.send(reply)
            return
        elif message.content == "!list":
            reply = ""
            for i in range(len(challenges)):
                reply += f"{challenges[i]["name"]}: {challenges[i]["url"]}\n"
            await message.channel.send(reply)
            return
        else:
            add_url = message.content.split(" ")[1]
            try:
                response = requests.get(add_url)
            except:
                reply = f"Unable to add: {add_url} please check it is a valid Coding Challenge"
                await message.channel.send(reply)
                return

            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.h1.text
            new_challenge = {"name":title,"url":add_url}
            challenges_dict["challenges"].append(new_challenge)
            with open("challenges.json", "w") as file:
                json.dump(challenges_dict, file, indent=4)
            reply = f"Added: {title}: {add_url}" 
            await message.channel.send(reply)
            return

client.run(TOKEN)