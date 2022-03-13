import os
from dotenv import load_dotenv

load_dotenv()
OPEN_API_GPT_SECRET_KEY = os.getenv('OPEN_API_GPT_SECRET_KEY')
