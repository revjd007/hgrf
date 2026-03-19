import os

# Bot token
token = os.getenv("DISCORD_BOT_TOKEN", "")

# The password for use /restore
recover_key = os.getenv("RECOVER_KEY", "recovkeydonotsharePLEASECHANGETHIS")

# Your guildid, used for restore and role adding
guildid = os.getenv("GUILD_ID", "")

# The verified role id
roleid = os.getenv("ROLE_ID", "")

# Your application's client id | Under the OAuth2 Tab in the dev portal
CLIENT_ID = os.getenv("CLIENT_ID", "")

# Your application's client secret | Under the OAuth2 Tab in the dev portal
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")

# Your webserver's url | Example 1: http://localhost:3000 / Example 2: https://verify.koma4k.xyz
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")

# Your webserver's IP | Recommend leaving it set to 127.0.0.1
WEB_IP = os.getenv("WEB_IP", "127.0.0.1")

# Port to host webserver on (if no port is set then it will default to port 3000)
WEB_PORT = int(os.getenv("PORT", "3000"))

# Your webserver's url + /callback | DO NOT CHANGE THIS | MAKE SURE TO ADD THIS REDIRECT TO THE DEVELOPER PORTAL!!
REDIRECT_URI = BASE_URL + '/callback'

# Don't change this
oauth2_url = f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify%20guilds%20guilds.join&state={guildid}"

# Don't change this
API_ENDPOINT = "https://discord.com/api/v9"

BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'