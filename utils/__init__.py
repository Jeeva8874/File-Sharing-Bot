from pyrogram import Client
import pyromod.listen
from config import *
from os import getcwd

Bot = Client(
    name='Saranam',
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=TG_BOT_TOKEN,
    sleep_threshold=SLEEP_THRESHOLD,
    workers=WORKERS
)

multi_clients = {}
work_loads = {}
