from .bot import dispatcher

def register_message_handlers():
    @dispatcher.message_handler(commands=['start', 'help'])
    async def send_welcome(message):
        await message.reply("Hello world!")

    @dispatcher.message_handler(commands=['raise', 'error'])
    async def send_error(message):
        raise Exception("Random error!")

    @dispatcher.message_handler()
    async def echo(message):
        await message.reply(f"Echo: {message.text}")
