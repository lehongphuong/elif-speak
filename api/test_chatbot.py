import time
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
start = time.time()
# Get a response to an input statement
chatbot = ChatBot('HelloIT',
                 storage_adapter='chatterbot.storage.SQLStorageAdapter',
                 database_uri='sqlite:///database.sqlite3')
output= chatbot.get_response("Hello, how are you today?")
print(output)
print(time.time() - start)
