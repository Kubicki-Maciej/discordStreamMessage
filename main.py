import discord
from discord.ext import commands
from bot_token import token
from users import load_ids, save_ids
global w

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
intents.typing = False
intents.presences = False
intents.members = True

# client = discord.Client(intents=intents)

client = commands.Bot(intents=intents, command_prefix='/')





@client.event
async def on_ready():
    print('________________')
    print(' Bot just run'  )
    print('________________')


@client.command()
async def message(ctx, user:discord.Member, *, message=None):
    print(user)
    print('wyslano wiadomosc')
    message = "STRIM ON"
    embed = discord.Embed(title=message)
    pass

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content.startswith('!add_me_to_stream'):
        user = message.author
        list_of_ids = load_ids('ids.json')
        if user.id in list_of_ids:
            print('user is in list')
            await user.send('User alredy in stream list')
        else:
            list_of_ids.append(user.id)
            save_ids('ids.json', list_of_ids)
            await user.send('User added to stream list')

def send_message_to_all_booked_users():

    pass


@client.event
async def on_ready():
    
    await client.wait_until_ready()
    
    list_of_ids = load_ids('ids.json')
    print(list_of_ids)
    if list_of_ids:
        print('jest lista')
    if list_of_ids:
        for user_id in list_of_ids:
            user = client.get_user(user_id)
            await user.send("stream is on") 

client.run(token=token)
