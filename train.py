# -*- coding: utf-8 -*-

from chatterbot import ChatBot


from chatterbot.trainers import *

#Replace ChatBot name with one of your choice.

chatbot = ChatBot("Bot")
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)
