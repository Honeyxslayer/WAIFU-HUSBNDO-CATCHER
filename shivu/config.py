class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6624008600"
    sudo_users = "6624008600", "5208708688"
    GROUP_ID = -1002093059683
    TOKEN = "6939032035:AAH7uosZb9v05Iy6DULV2L_Wt2niVpJVduQ"
    mongo_url = "mongodb+srv://kaneki01:jiNOXXMlwJzDyYvQ@kaneki.nca4u2n.mongodb.net/"
    PHOTO_URL = ["https://graph.org/file/de583389881d34e4b51e5.jpg", "https://graph.org/file/3eb21ef48c323d0b3f0c5.jpg"]
    SUPPORT_CHAT = "insanesociety"
    UPDATE_CHAT = "insaneupdate"
    BOT_USERNAME = "insane_catcher_bot"
    CHARA_CHANNEL_ID = "1002068358722"
    api_id = 24341346
    api_hash = "2e0526c7dbae85722313845219600c56"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
