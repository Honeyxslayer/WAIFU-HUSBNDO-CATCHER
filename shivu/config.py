class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5934011554"
    sudo_users = "5934011554", "7142432455", "6438889828"
    GROUP_ID = -1002090005496
    TOKEN = "7081317823:AAGPUMqbmB5fuMzS-uN0rija-9gJa4lJvIA"
    mongo_url = "mongodb+srv://insanekaneki7:w86O8Q2f7pGEdWYR@cluster0.fxcecdz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://graph.org/file/c8793f5a74801abd370fd.jpg", "https://graph.org/file/09f2c059d8bc0a7d95fb8.jpg"]
    SUPPORT_CHAT = "insanesociety"
    UPDATE_CHAT = "honey_networks"
    BOT_USERNAME = "duro_robot"
    CHARA_CHANNEL_ID = "1002136697049"
    api_id = 29044160
    api_hash = "b93797389eab3cec8c697ae4f2418466"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
