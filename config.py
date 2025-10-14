import os
from typing import List

API_ID = os.environ.get("API_ID", "22367239")
API_HASH = os.environ.get("API_HASH", "b181c41155ee1e3798d5de44673bb1a7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8313516165:AAEevLh-17tE7l5yqXa8K_4qsvGZfajyiuU")
ADMIN = int(os.environ.get("ADMIN", "8127363932"))
PICS = (os.environ.get("PICS", "")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003064804454"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://sunilkumarpalaka972_db_user:e4ZYD1IeAGg7vvi1@cluster0.j8z7o9j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "sunilkumarpalaka972_db_user")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "fales"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1003114110211").split())) # Add Multiple channel ids
