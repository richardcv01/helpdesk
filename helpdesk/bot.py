from mmpy_bot import Bot, Settings
from .my_plugin import MyPlugin



plag = MyPlugin()
#plag.set_plug()

bot = Bot(
    settings=Settings(
        MATTERMOST_URL = "http://mattermost.dbr.gov.ua",
        MATTERMOST_PORT = 80,
        #BOT_TOKEN = "pn3pzam6bb8adrexymn8uhad3e",
        BOT_TOKEN = "q51dn8wnupgrbfw6iopqi34xcr",
        BOT_TEAM = "helpdesk_bot",
        SSL_VERIFY = False,
    ),  # Either specify your settings here or as environment variables.
    plugins=[plag],  # Add your own plugins here.
)



