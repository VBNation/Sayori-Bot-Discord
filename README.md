# Sayori-Bot Discord Wrapper
A discord bot wrapper for the Sayori-Bot main project

This code repo utilizes a modified version of MokouBot <br>
Repo: https://github.com/benoxoft/MokouBot

## Installation
Install python >= 3.5

##### Install dependencies:
```
pip install -r requirements.txt
```

To utilize the voice response, install ffmpeg.
Edit your PATH environment variable if needed.

## Setting up the bot

##### Get an API key
Create a new application here: https://discordapp.com/developers/applications/me#top <br>
Find the api key in the new application under Token and copy-paste it into a new file named API_KEY.txt located in the project root directory.<br>

##### Edit config.py

Edit BOTID <br>
Edit OWNERID <br>
Edit ChatBot name

##### Edit train.py

Edit your bot's name to the one set in config.py

## Running the bot

##### Train the bot with the English Corpus
```
python3 train.py
```

**-----OR-----**

##### Train the bot with 4chan:
The bot grabs conversations from threads on 4chan. You can configure from which board to get the data in config.py <br>
By default it grabs conversations from those boards:
```
SFW_BOARDS = ['jp', 'a', 'v',]
NSFW_BOARDS = ['b', 'pol']
```
The training script will also grab images from the SFW boards and place them in the images/ directory. If you do not want to download the images (1-2 GB), edit config.py and remove all the boards from SFW_BOARDS and place them in NSFW_BOARDS like so:
```
SFW_BOARDS = []
NSFW_BOARDS = ['jp', 'a', 'v', 'b', 'pol']
```
When ready start training:
```
python 4chan_train.py
```

## Start the bot
```
python bot.py
```

##### Invite the bot to your server
Go there and invite your bot: https://discordapp.com/oauth2/authorize?client_id={YOUR_CLIENT_ID}&scope=bot&permissions=0 <br>
Change {YOUR_CLIENT_ID} to the client ID of your bot

## Command List
Type "help" starting with your command prefix <br>
Ex: <br>
```
~help
```
This command will return a PM message to the person who sent it. The list can be found in the features directory.
## How to communicate
##### Textual communication
The bot picks up messages that include its Discord name. <br>
The bot will not respond to the name you included in the config.py or bot.py files <br>
##### Verbal response
To get the bot to respond verbally, join a voice channel and type in ```join``` starting with your command prefix stated in config.py (Default COMMANDPREFIX = '~').
