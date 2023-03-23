from dotenv import load_dotenv
import os

load_dotenv()

GHOST_API_KEY = os.environ.get("GHOST_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
MONGODB_CONNECTION = os.environ.get("MONGODB_CONNECTION")
