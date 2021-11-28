# Discord Scraper

A python script for scraping solana wallet addresses in a discord server.

## Requirements
- discord.py
- re
- json
- os
- dotenv


## How It Works?
A Discord bot client is initialized. This client works with the specified discord bot token. When an event is received, all messages in the channel are retrieved with the specified channel id. The received messages are checked one by one with regexp within the for loop. If it matches with the regexp, the discord id of the author of the message and the message are stored as a dictionary which is used to store key:value pairs and this dict is appended to a list. After all messages are checked, this list is written to the json file.




## Installation
```
git clone https://github.com/1-0-1-Labs/discord_parser
cd discord_parser
pip3 install -r requirements.txt
```

## Usage
```python3 dc-scraper.py```
```
user@pc:~$ python3 scrape_dc.py 
[INFO] Logged in as my_lovely_bot#3886
[INFO] JSON data is written to wallet_addresses.json
```

## Creating a Discord Bot & Fetching Bot's Token
After entering [here](http://discordapp.com/developers/applications), create a new application. Enter the bot settings of the application you created and click "Add Bot". After adding a bot, click "Click to Reveal Token" to see the bot's token below. Detailed info [here](https://realpython.com/how-to-make-a-discord-bot-python/#creating-an-application)

## Adding the Bot to a Discord Server
To add your bot to a discord server, you should know its client id. You can find it from the OAuth2 settings of the application that you created before. Detailed info [here](https://www.alphr.com/add-bots-discord-server/). After finding the client id, just replace with *YOUR_CLIENT_ID* in the following URL.
```https://discordapp.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=0```

## Finding the ID of a Discord Channel
Go to your discord settings > advanced settings and enable "Developer Mode". After enabling the developer mode, right click to the channel that you want to find its id and click "Copy ID". Detailed info [here](https://www.swipetips.com/how-to-get-channel-id-in-discord/)

## Using Discord Scraper 
Firstly create a discord bot and add it to your discord server. After adding it to your discord server get ID of the channel that you want to scrape. Clone this repo to your device and change enviroment variables (channel id and bot token) which are in ".env" file. Execute the python script and thats all!

