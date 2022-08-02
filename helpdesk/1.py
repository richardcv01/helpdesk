import asyncio
import telegram

API_TOKEN = '5541780288:AAFDKbfLXfkuhDqY0wWHfdlx8WqlG-c3SWA'

async def main():
    bot = telegram.Bot(API_TOKEN)
    async with bot:
        await bot.send_message(text='Hi John!', chat_id=1234567890)


asyncio.run(main())