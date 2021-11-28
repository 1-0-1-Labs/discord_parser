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



