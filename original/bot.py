from telethon import TelegramClient, events
#=========================#
api_id = ايدي 
api_hash = 'هاش' 
client = TelegramClient('dudrd', api_id, api_hash)
@client.on(events.NewMessage)
async def Saif(event):
    if event.is_private:
        await event.respond("""اهلا حبي 
انا ماموجود هسه مفعل تلقائي
من اجي ارد عليك 👾""")
with client:
    print('run .')
    client.run_until_disconnected()