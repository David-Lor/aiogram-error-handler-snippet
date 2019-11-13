import os
import aiogram
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BOT_TOKEN")

bot = aiogram.Bot(token=token)
dispatcher = aiogram.Dispatcher(bot)
