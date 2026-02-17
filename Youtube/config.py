import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8427108179:AAHhEN3I4Zup6YmQG6bkL-ekqYbL9eqaoRo")
    API_ID = int(os.environ.get("API_ID", '34724970'))
    API_HASH = os.environ.get("API_HASH", "f240eae7c60e8e30c17203ab0e052f7e")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1003791757895")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
