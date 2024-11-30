#(©)NovaXTG
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7548795553:AAGPlTEyUZ4JDttELUvAEtn4psGlFMwhuQQ-Ucl3nM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22977776"))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "HeartFileStore_bot") #without @
BOT_NAME = os.environ.get("BOT_NAME", "ɴᴏᴠᴀ | ғɪʟᴇ sʜᴀʀɪɴɢ ʙᴏᴛ")
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2ac7223d720bdeec757cbc88ced57224")
PIC = os.environ.get("PIC", "https://telegra.ph/file/c4492791ab1025e3f2602.jpg")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002480489590"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6762558871"))
#Port
PORT = os.environ.get("PORT", "8080")
#Shortener
SHORTENER_WEBSITE = os.environ.get('SHORTENER_WEBSITE', 'tnshort.net')
SHORTENER_API = os.environ.get('SHORTENER_API', 'b6aace46d40c605fff8e0cafbcd8fbe416851f4d')
TUTORIAL_VIDEO = os.environ.get("TUTORIAL_VIDEO", "https://telegra.ph/file/ff2d9ea3e0c33e1833300.mp4")
#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jeevanantham8157:1055221@leechbot.gpkuo.mongodb.net/?retryWrites=true&w=majority&appName=Leechbot")
DB_NAME = os.environ.get("DATABASE_NAME", "AutoPost")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
CHANNEL_ONE = int(os.environ.get("CHANNEL_ONE", "0"))
CHANNEL_TWO = int(os.environ.get("CHANNEL_TWO", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ ᴅᴜᴅᴇ 🥂 ɪ ᴀᴍ ᴀ ʀx ʟɪɴᴋᴢᴢ ғʟɪᴍ ᴘʀᴏᴠɪᴅᴇʀ ʙᴏᴛ, ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ɪɴᴛᴇʀᴇsᴛɪɴɢ ғᴇᴀᴛᴜʀᴇs. ɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ ᴛᴏ ʙᴜʏ ᴍᴇ, ᴄᴏɴᴛᴀᴄᴛ <a href=https://t.me/NovaXTG>ɴᴏᴠᴀxᴛɢ</a> 👨🏼‍💻</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6762558871").split()):
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
ADMINS.append(6762558871)
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
BIN_CHANNEL = int(os.getenv('BIN_CHANNEL', '-1002389516001'))  #Need to put same id of stream bot log channel
PORT = int(os.getenv('PORT', '443'))
BIND_ADDRESS = str(os.getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "1200"))  # 20 minutes
OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6762558871").split())
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
