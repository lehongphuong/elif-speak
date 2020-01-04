from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('HelloIT',
                 storage_adapter='chatterbot.storage.SQLStorageAdapter',
                 database_uri='sqlite:///database.sqlite3')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")

trainer.train("./english_conversations.json")
trainer.train("./movie_conversation.json")