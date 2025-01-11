import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("LD_PRELOAD")
DOMAIN = os.getenv("LD_PRELOAD")

print(TOKEN) #AQAAAAAz55vbAAdBSHeydEoSe0fclxSSABT
print(DOMAIN)
