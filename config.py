import os

from chatterbot import ChatBot
import logging
logging.basicConfig(level=logging.INFO)


# configure how the bot train and retrieve responses
chatbot = ChatBot(
    'Sayori',
    trainer='chatterbot.trainers.ListTrainer',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
	filters=["chatterbot.filters.RepetitiveResponseFilter"],
	preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
		'chatterbot.preprocessors.unescape_html',
		'chatterbot.preprocessors.convert_to_ascii',
    ],
	logic_adapters=[
        #'chatterbot.logic.BestMatch',
		
		{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.'
        },
		
		"chatterbot.logic.MathematicalEvaluation",
        #"chatterbot.logic.TimeLogicAdapter",
    ],
	
)

COMMANDPREFIX = '~'
BOTID = 'Discord Bot ID'
OWNERID = 'Your Discord ID'


#
PROCESS_POOL_EXECUTOR_COUNT = 3
WAIT_TIME_BEFORE_TYPING = 2
WAIT_TIME_RESPONSE_READY = 0.3

# Images are downloaded from SFW boards. Images are not downloaded from NSFW boards
SFW_BOARDS = ['jp', 'a', 'v',]
NSFW_BOARDS = ['b', 'pol']

# Messages that aren't in the corresponding length will be discarded from the training data
MIN_MESSAGE_LENGTH = 4
MAX_MESSAGE_LENGTH = 256

# Replies that aren't in the corresponding length will be discarded from the training data
MIN_REPLY_LENGTH = 4
MAX_REPLY_LENGTH = 140

# 4chan demand to not make more than one request per second to their API
SLEEP_TIME_4CHAN = 1.2
