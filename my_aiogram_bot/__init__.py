import aiogram
from .bot import dispatcher
from .message_handlers import register_message_handlers
from .error_handlers import register_error_handlers

def run():
    register_message_handlers()
    register_error_handlers()
    aiogram.executor.start_polling(dispatcher, skip_updates=True)
