#(©)NovaXTG
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5743107971:AAGgpOw0Ga9mZIhcxCWXUhJDUwox-Ucl3nM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9321645"))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "RolexFileSharing_Bot") #without @
BOT_NAME = os.environ.get("BOT_NAME", "ɴᴏᴠᴀ | ғɪʟᴇ sʜᴀʀɪɴɢ ʙᴏᴛ")
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6a1b5084e59012093525c2443880a09a")
PIC = os.environ.get("PIC", "https://telegra.ph/file/c4492791ab1025e3f2602.jpg")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001877742594"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5296610774"))
#Port
PORT = os.environ.get("PORT", "8080")
#Shortener
SHORTENER_WEBSITE = os.environ.get('SHORTENER_WEBSITE', 'tnshort.net')
SHORTENER_API = os.environ.get('SHORTENER_API', 'b6aace46d40c605fff8e0cafbcd8fbe416851f4d')
TUTORIAL_VIDEO = os.environ.get("TUTORIAL_VIDEO", "https://telegra.ph/file/ff2d9ea3e0c33e1833300.mp4")
#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "tutorial")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
CHANNEL_ONE = int(os.environ.get("CHANNEL_ONE", "0"))
CHANNEL_TWO = int(os.environ.get("CHANNEL_TWO", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ ᴅᴜᴅᴇ 🥂 ɪ ᴀᴍ ᴀ ʀx ʟɪɴᴋᴢᴢ ғʟɪᴍ ᴘʀᴏᴠɪᴅᴇʀ ʙᴏᴛ, ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ɪɴᴛᴇʀᴇsᴛɪɴɢ ғᴇᴀᴛᴜʀᴇs. ɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ ᴛᴏ ʙᴜʏ ᴍᴇ, ᴄᴏɴᴛᴀᴄᴛ <a href=https://t.me/NovaXTG>ɴᴏᴠᴀxᴛɢ</a> 👨🏼‍💻</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5296610774 1232844084 5517793030").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʜᴇʟʟᴏ ᴅᴜᴅᴇ 🥂 ɪ ᴀᴍ ᴀ ʀx ʟɪɴᴋᴢᴢ ғʟɪᴍ ᴘʀᴏᴠɪᴅᴇʀ ʙᴏᴛ, ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ɪɴᴛᴇʀᴇsᴛɪɴɢ ғᴇᴀᴛᴜʀᴇs. ɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ ᴛᴏ ʙᴜʏ ᴍᴇ, ᴄᴏɴᴛᴀᴄᴛ <a href=https://t.me/NovaXTG>ɴᴏᴠᴀxᴛɢ</a> 👨🏼‍💻</b>")
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>ɴᴀᴍᴇ</b> : {filename}\n\n ɴᴏᴛᴇ: ᴀꜰᴛᴇʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ꜰɪʟᴇꜱ, ꜱᴀᴠᴇ ᴛʜᴇ ꜰɪʟᴇ ᴛᴏ ɢᴀʟʟᴇʀʏ ᴀɴᴅ ᴄʟɪᴄᴋ ᴛʜᴇ ᴅᴇʟᴇᴛᴇ ʙᴜᴛᴛᴏɴ, ᴅᴏɴ'ᴛ ᴄʟɪᴄᴋ ʙᴇꜰᴏʀᴇ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ꜰɪʟᴇꜱ, ɪꜰ ᴜ ᴅᴏɴ'ᴛ ᴡᴀɴᴛ ᴛʜɪꜱ ꜰɪʟᴇ ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴅᴇʟᴇᴛᴇ ʙᴜᴛᴛᴏɴ")
#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>⚠ ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀ ᴍᴇssᴀɢᴇs, ɪᴛs ᴏɴʟʏ sᴜᴘᴘᴏʀᴛs ᴅᴏᴄᴜᴍᴇɴᴛ | ᴠɪᴅᴇᴏs | ᴘʜᴏᴛᴏs</b>"
ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
MULTI_CLIENT = False
name = str(os.getenv('name', 'saranam'))
SLEEP_THRESHOLD = int(os.getenv('SLEEP_THRESHOLD', '60'))
WORKERS = int(os.getenv('WORKERS', '3'))
BIN_CHANNEL = int(os.getenv('BIN_CHANNEL', '-1001877742594'))  #Need to put same id of stream bot log channel
PORT = int(os.getenv('PORT', '443'))
BIND_ADDRESS = str(os.getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "1200"))  # 20 minutes
OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5517793030 5517793030").split())
NO_PORT = bool(os.getenv('NO_PORT', False))
APP_NAME = None
FQDN = "stream.kr-linkzzz.workers.dev"
RXDN = "direct.kr-linkzzz.workers.dev"
RXL = "https://{}".format(RXDN)
HAS_SSL = bool(os.getenv('HAS_SSL', True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
