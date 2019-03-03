import asyncio
from features import *
from concurrent.futures import ProcessPoolExecutor
import os
import sys
import unicodedata
import requests
from gtts import gTTS
import youtube_dl
from config import BOTID
from config import OWNERID
from config import COMMANDPREFIX

import discord

from config import chatbot, PROCESS_POOL_EXECUTOR_COUNT, WAIT_TIME_BEFORE_TYPING, WAIT_TIME_RESPONSE_READY, COMMANDPREFIX, BOTID

print("Starting process")
#f = open("vc.wav", "wb")
client = discord.Client()
ppool = ProcessPoolExecutor(PROCESS_POOL_EXECUTOR_COUNT)

async def start(self):
    discord.opus.load_opus(self.opus_library)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Sayori Discord Wrapper"))
	

def generate_response(message):
    return chatbot.get_response(message)


async def reply_to_message(message):
    print("Got:", message.content.encode('utf-8'))
    msg = message.content.lower().replace(client.user.name.lower(), '').replace(client.user.mention, '')
    response_gen = asyncio.get_event_loop().run_in_executor(ppool, generate_response, msg)
    await asyncio.sleep(WAIT_TIME_BEFORE_TYPING)
    while not response_gen.done():
        await asyncio.sleep(WAIT_TIME_RESPONSE_READY)
        await client.send_typing(message.channel)
    response = response_gen.result()
    print("Sending:", response)
    filename = ''
    if ' <img>' in str(response):
        response, filename = str(response).split(' <img>')
    await client.send_message(message.channel, message.author.mention + ' ' + str(response))
    print('file:', filename)
    if filename and os.path.exists(os.path.join('images', filename)):
        with open(os.path.join('images', filename), 'rb') as f:
            await client.send_file(message.channel, f)
#sayori tts
    tts = gTTS(text=str(response),lang='en')
    tts.save('msg.mp3')
	
    player = voice.create_ffmpeg_player('msg.mp3')
    player.start()
	
#sayori speech recognition
    # await VoiceClient.poll_voice_ws(f.write())
	
@client.event		
async def on_message(message):

# If the message author isn't the bot and the message starts with the
    # command prefix ('!' by default), check if command was executed
    if message.author.id != BOTID and message.content.startswith(COMMANDPREFIX):
        # Remove prefix and change to lowercase so commands aren't case-sensitive
        message.content = message.content[1:].lower()

        # Shuts the bot down - only usable by the bot owner specified in config
        if message.content.startswith('shutdown') and message.author.id == OWNERID:
            await client.send_message(message.channel, 'Shutting down. Bye!')
            await client.logout()
            await client.close()
        ########## VOICE COMMANDS ##########

        # Will join the voice channel of the message author if they're in a channel
        # and the bot is not currently connected to a voice channel
        elif message.content.startswith('join'):
            if message.author.voice_channel != None and client.is_voice_connected(message.server) != True:
                global currentChannel
                global player
                global voice
                currentChannel = client.get_channel(message.author.voice_channel.id)
                voice = await client.join_voice_channel(currentChannel)

            elif message.author.voice_channel == None:
                await client.send_message(message.channel, 'You are not in a voice channel.')

            else:
                await client.send_message(message.channel, 'I am already in a voice channel. Use !leave to make me leave.')

        # Will leave the current voice channel
        elif message.content.startswith('leave'):
            if client.is_voice_connected(message.server):
                currentChannel = client.voice_client_in(message.server)
                await currentChannel.disconnect()
		# Will play music using the following words as search parameters or use the
        # linked video if a link is provided
        elif message.content.startswith('play'):
            if message.author.voice_channel != None:
                if client.is_voice_connected(message.server) == True:
                    try:
                        if player.is_playing() == False:
                            print('not playing')
                            player = await voice.create_ytdl_player(youtubeLink.getYoutubeLink(message.content))
                            player.start()
                            await client.send_message(message.channel, ':musical_note: Currently Playing: ' + player.title)

                        else:
                            print('is playing')

                    except NameError:
                        print('name error')
                        player = await voice.create_ytdl_player(youtubeLink.getYoutubeLink(message.content))
                        player.start()
                        await client.send_message(message.channel, ':musical_note: Currently Playing: ' + player.title)

                else:
                    await client.send_message(message.channel, 'I am not connected to a voice channel. Use !join to make me join')

            else:
                await client.send_message(message.channel, 'You are not connected to a voice channel. Enter a voice channel and use !join first.')

        # Will pause the audio player
        elif message.content.startswith('pause'):
            try:
                player.pause()

            except NameError:
                await client.send_message(message.channel, 'Not currently playing audio.')

        # Will resume the audio player
        elif message.content.startswith('resume'):
            try:
                player.resume()

            except NameError:
                await client.send_message(message.channel, 'Not currently playing audio.')

        # Will stop the audio player
        elif message.content.startswith('stop'):
            try:
                player.stop()

            except NameError:
                await client.send_message(message.channel, 'Not currently playing audio.')
		# Help Message, sends a personal message with a list of all the commands
        # and how to use them correctly
        elif message.content.startswith('help'):
            await client.send_message(message.channel, 'Sending you a PM!')
            await client.send_message(message.author, helpMessage.helpMessage)


    if client.user.mention == message.author.mention:
        return
    if not (client.user.name.lower() in message.content.lower() or client.user.mention in message.content):
        return

    await reply_to_message(message)

if __name__ == '__main__':
    if not os.path.exists('API_KEY.txt'):
        print("Couldn't find API_KEY.txt.")
        print("Create a file named API_KEY.txt and paste your API key in the file to connect the bot to Discord")
        sys.exit(0)

    with open('API_KEY.txt', 'r') as api_key_file:
        API_KEY = api_key_file.read().strip()

    while True:
        try:
            client.run(API_KEY)
        except Exception as e:
            print(e)
            import time
            time.sleep(10)
            client = discord.Client()
		  # Press ctrl-c or ctrl-d on the keyboard to exit
        #except (KeyboardInterrupt, EOFError, SystemExit):
         #   break
			
