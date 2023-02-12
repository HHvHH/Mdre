import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "19351645"))
    API_HASH = os.environ.get("API_HASH", "359f66a067069b8b5c482df6a8a4e3b8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "i2i2bot")
    SUPPORT = os.environ.get("SUPPORT", "hedrr")
    CHANNEL = os.environ.get("CHANNEL", "hedrr")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/16c8c27938bc7ac235436.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/16c8c27938bc7ac235436.jpg")
