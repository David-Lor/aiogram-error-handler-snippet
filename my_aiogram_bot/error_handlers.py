from .bot import dispatcher

def register_error_handlers():
    @dispatcher.errors_handler()
    async def global_error_handler(update, exception):
        await update.message.reply(f"Error happened! ({exception})")
