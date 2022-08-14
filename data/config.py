from environs import Env

# environs kitaphanasinan paydalanu
env = Env()
env.read_env()

# .env fayl ishhindegi osilardi oqi'miz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # admindar tizimi
IP = env.str("ip")  # Hosting ip address
