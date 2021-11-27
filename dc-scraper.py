from discord.ext.commands import Bot
import discord
import re
import json
import os
from dotenv import load_dotenv

client = Bot(command_prefix='!')  # Creates a client for the discord bot
data = []  # Stores multiple dicts which are discord ids and wallet addresses

load_dotenv()

token = os.getenv('DC_BOT_TOKEN')  # Auth token of the discord bot
channel_id = os.getenv('DC_CHANNEL_ID')  # Discord channel id which is for parsing
regexp = os.getenv('REGEXP')  # Solana wallet addr regexp
json_filepath = os.getenv('JSON_FILEPATH')  # Filepath for dumping json data
info = "[INFO]"  # Only for informative output, nothing more


@client.event  # Works when an event recieved from declared discord client
async def on_ready():  # This function works async when client recieves an event
    print('{0} Logged in as {1.user}'.format(info, client))  # Prints username of the discord bot, for e.g "my_lovely_bot#1234"

    channel = client.get_channel(int(channel_id))  # Gets channel
    messages = await channel.history(limit=None).flatten()  # Gets all messages from channel, no limit

    for message in messages:
        if re.match(regexp, str(message.content)):  # Checks message content matches the regexp
            msg = {
                "discord_id": message.author.id,  # Discord id of message author
                "wallet_address": message.content  # Solana wallet address
            }
            data.append(msg)  # Appends dict data to a list

    with open(json_filepath, 'w') as outfile:  # Opens json file in write-only mode.
        json.dump(data, outfile, indent=4)  # Writes json data to a json file with indentation to make json file more human-readable
    print('{0} JSON data is written to {1}'.format(info, json_filepath))  # Prints filepath of the json file
    os._exit(0)  # Exits from the script successfuly, without any errors

client.run(token)

