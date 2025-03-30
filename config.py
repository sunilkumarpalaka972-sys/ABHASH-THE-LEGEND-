from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", ""))
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
IS_FSUB = bool(environ.get("FSUB", True))
AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]
