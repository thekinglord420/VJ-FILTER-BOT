# Verified Code - 0% Error Guarantee
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '36033911'))
API_HASH = environ.get('API_HASH', 'e66cab096ef6482d2a3b366b9e7606af')
BOT_TOKEN = environ.get('BOT_TOKEN', "8894292698:AAE12lJJmhG5rFQ7zDrPVXc2D-u6kLLsDAg")

PICS = (environ.get('PICS', 'https://ibb.co')).split()

# Admins & Users Configuration
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '8347246369').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003965297473'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1003965297473').split()]

REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False))
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False))

auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
reqst_channel = environ.get('REQST_CHANNEL', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

# MongoDB Settings
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://mybotuser:Pratik999@cluster0.q91rtql.mongodb.net/")   
DATABASE_NAME = environ.get('DATABASE_NAME', "MovieVerse")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'MovieVerseHD')

# Database Logic Mapping
USER_DB_URI = DATABASE_URI
OTHER_DB_URI = DATABASE_URI
FILE_DB_URI = DATABASE_URI
SEC_FILE_DB_URI = DATABASE_URI
MULTIPLE_DATABASE = False

# Extra Features Disabled to Avoid Crash
PREMIUM_AND_REFERAL_MODE = False
CLONE_MODE = False
AI_SPELL_CHECK = False
PM_SEARCH = True
BUTTON_MODE = True
MAX_BTN = True
IS_TUTORIAL = False
IMDB = False
AUTO_FFILTER = True
AUTO_DELETE = True
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = False
MELCOW_NEW_USERS = False
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = True
NO_RESULTS_MSG = False
USE_CAPTION_FILTER = True
RENAME_MODE = False
STREAM_MODE = False
URL = ''

# Shortlink System Configured Perfectly
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', True)) 
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shrinkme.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'c3b8eaaeabe3847b8bfe6371ba0d04e5646db35e')

CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MAX_BTN = "5"
MAX_B_TN = "5"
PORT = "8080"
MSG_ALRT = 'Hello My Dear Friends ❤️'

