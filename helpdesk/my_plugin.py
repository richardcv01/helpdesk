from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message
import click
import re
from .REQUEST import GET_tikets, UPDATE_tikets, get_id_user, get_stan_tiket


class MyPlugin(Plugin):

    def set_plug(self, text):
        self._text = text

    def _test_decorator(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            print(self._text)
            self.driver.create_post(channel_id="i4uawqja47rgip4kdrq7founir", message=self._text)
            return func(*args, **kwargs)

        return wrapper

    @_test_decorator
    def on_start(self):
    #def on_start(self):
    #def on_start(self):
    #def on_start(self):
        """Notifies some channel that the bot is now running."""
        #self.driver.create_post(channel_id="i4uawqja47rgip4kdrq7founir", message=message)
        self.driver.create_post(channel_id="i4uawqja47rgip4kdrq7founir", message='')
        #self.driver.create_post(channel_id="i4uawqja47rgip4kdrq7founir", message=1)
        print(111)


    @listen_to('hello')
    async def help_me(self, message: Message):
        print(message.sender_name)
        self.driver.reply_to(message, ("Hello_____ " + message.sender_name))

    @listen_to("^\\+\\ ([0-9]+)$", re.IGNORECASE)
    def done(self, message: Message, number: int):
    #def done(self, message: Message):
        user_id = str(get_id_user(message.sender_name))
        stan = UPDATE_tikets(number, "2", user_id)
        print('sat', stan)
        if stan:
            self.driver.reply_to(message, f"Заявка {number} виконана! " + message.sender_name)
        else:
            self.driver.reply_to(message, f"Заявка не існує")

    @listen_to("^\\*\\ ([0-9]+)$", re.IGNORECASE)
    def done_1(self, message: Message, number: int):
        # def done(self, message: Message):
        user_id = str(get_id_user(message.sender_name))
        stan = UPDATE_tikets(number, "3", user_id)
        print('sat', stan)
        if stan:
            self.driver.reply_to(message, f"Заявка {number} на виконанні! " + message.sender_name)
        else:
            self.driver.reply_to(message, f"Заявка не існує")

    @listen_to("^([0-9]+)$", re.IGNORECASE)
    def taken_for_execution(self, message: Message, number: int):
        stan = get_stan_tiket(number)
        print('sat', stan)
        self.driver.reply_to(message, f"Заявка {number} ! " + stan)


