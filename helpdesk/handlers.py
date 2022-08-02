import aiogram

async def send_(message: types.Message):
    user_should_be_notified = -680022832
    await message.reply(message.chat.id)
#         print(message)
#         await self.bot.send_message(user_should_be_notified, message)