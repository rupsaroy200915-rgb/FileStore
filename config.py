import logging
import os
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = os.environ.get('PORT', '5010')
OWNER_ID = int(os.environ.get('OWNER_ID', 6896698075))

MSG_EFFECT = 5046509860389126442

SHORT_URL = os.environ.get('SHORT_URL', "gplinks.com") 
SHORT_API = os.environ.get('SHORT_API', "e07aec576df2a9ed36f1b94b8017cc53b792496f") 
SHORT_TUT = os.environ.get('SHORT_TUT', "https://t.me/+dfEc0fVvm4s3NGY1")

# Bot credentials
SESSION = os.environ.get('SESSION', "")
TOKEN = os.environ.get('TOKEN', "")
API_ID = int(os.environ.get('API_ID', 37687219)) 
API_HASH = os.environ.get('API_HASH', "d4d343d55bd3c3f645200c4c81be7867") 
WORKERS = int(os.environ.get('WORKERS', 5))

DB_URL = os.environ.get('DB_URL', "mongodb+srv://RupsaRoy:ram123@cluster0.msvefse.mongodb.net/?appName=Cluster0") 
DB_NAME = os.environ.get('DB_NAME', "Ram")

FSUBS = [[-1003751570614, True, 10]] 
DB_CHANNEL = int(os.environ.get('DB_CHANNEL', -1003578999463))

AUTO_DEL = 300
ADMINS = [6896698075, 8229228616]
DISABLE_BTN = True
PROTECT = True

MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ~ <blockquote>ʟᴏᴠᴇ KATHA? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ aʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: @+dfEc0fVvm4s3NGY1 \n <blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/+dfEc0fVvm4s3NGY1'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n›› ᴏᴡɴᴇʀ: @ProYato\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @cosmic_freak</b></blockquote>",
    "REPLY": "<b>For More Join - @+dfEc0fVvm4s3NGY1</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "",
    "FSUB_PHOTO": "",
    "SHORT_PIC": "",
    "SHORT": ""
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
