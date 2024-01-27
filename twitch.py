from shared import twitch_clientid, twitch_oauth, channel_id
from twitchio.ext import commands
from openai import get_response


bot = commands.Bot(
    token=twitch_oauth,  # Use 'token' instead of 'irc_token'
    client_id=twitch_clientid,
    nick='asdawd',
    prefix='!',
    initial_channels=[channel_id]
)
#When The bot is ready Send Print...
@bot.event()
async def event_ready():
    print(f'Logged into Twitch | {bot.nick}')

#As the API Documents says it's a message event, it will get the author name and the content and display with print, as soon someones sends a message.
@bot.event()
async def event_message(message):
    user_input = message.content
    get_response(user_input)
    await bot.handle_commands(message)

