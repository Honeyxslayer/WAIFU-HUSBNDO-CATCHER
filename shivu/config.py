class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5934011554"
    sudo_users = "5934011554", "7142432455", "6438889828"
    GROUP_ID = -1002090005496
    TOKEN = "7148259690:AAFQ_ItaRVHPJ1iW_S92OkJr-7M0VTfqxi0"
    mongo_url = "mongodb+srv://insanekaneki7:w86O8Q2f7pGEdWYR@cluster0.fxcecdz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://graph.org/file/c8793f5a74801abd370fd.jpg", "https://graph.org/file/09f2c059d8bc0a7d95fb8.jpg", "https://graph.org/file/987595a3820c77a6e13f2.jpg", "https://graph.org/file/4b0a579e078b309c75e7d.jpg", "https://graph.org/file/8db16140024c4d1820b0c.jpg", "https://graph.org/file/b6975f9b5d51bfcbcc40d.jpg", "https://graph.org/file/704bddb445785d17847f3.jpg"]
    SUPPORT_CHAT = "insanesociety"
    UPDATE_CHAT = "honey_networks"
    BOT_USERNAME = "Collect_yourwaifu_bot"
    CHARA_CHANNEL_ID = "1002136697049"
    api_id = 29044160
    api_hash = "b93797389eab3cec8c697ae4f2418466"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
