import os,sys,nest_asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

nest_asyncio.apply()
profile="prod"

api_id = 8735668
api_hash = 'cc6f8af5232a2c2a501674639145b83b'
dialog_count = 10
dev="1BVtsOH0Bu1TPlJVZWWAHz_iv_VH9aw7fNnDsLqp7y2fQeP73DNFDJ5vlUE0eT3JdNqUwG1qBPWTtleXrOEnf_cdECIK5OOmQxD2tHwHQLUugtf-wee7klcNnc6tEwJh5-bT19sck9C0JgV4-W0Lk479aItionRv1j7e67uaaDbi96o654LH3yQGcvzfmfbMO0OmASsFtwshLm0pKEiTdlXlG60wKFrIFNmqWJdrqh0McZT_6t2cVNrez0836EIksdTaQbyRz7iiT2-wdxBUztsrf3SJ6qJPwHYkk7Hg4rVSb6lOhkV2NlfFJWqi7f13Z68GhIsPAjj0jLkyXNcNsuHVnLAmfoBc="
prod="1BVtsOH0Bu2YkM9F0sysm4RItLyPglN-08TSMdM7ZWMTSrj07x5gIRaFI6lQqaNb3TCzs9TXIzHGYaLOgl6Q-7zVktjhmoaagYNanCnOoNnkiT-M7_DnmiXdyLPtdnAgxP8yQwdTNRWpswfXymZNBdbdgdX6_udY5oiYzTc3KqkKxY9-KKvxtCi0L_6TViqz2d1zvRYKuJprD2haGurDkptTGFUb83uyeQBe1RhbPpSyypPnCBNtQ4OMvVhxLgIoxeCPwVuf3BZQqzX9LjqvW4z--fvPdBl536KcwJ6xSxmtPzbuclTczx1vcn2OwAEYGeuMgLpRbM2IpoOBYo6ukhe_f3Ot-DgE="
if(profile=="dev"):
    from_channels={"@dev-sender":-1001773695108,"group@dev-sender":-717766555}
    to_channels={"@dev-receiver":-1001541896616}
else:
    from_channels={"@prod-sender":-1001527921225,"@gocareers":-1001299734537,"@codeencodes_":-1259516307,"group@jobseekers_helpinghands":-1001533926441}
    to_channels={"@socalledhappenings":-1001510149016}
others=["price","coupon","discount","congratulations","congrats","offer","follow","join","joinchat","welcome","telegram","t.me","telegram.me","party","desk","help","money","donate","voice","bot","hurry","soon","missout","discount","limited","meet.google.com","zoom.us","message me","milaap","gocareers"]

def session():
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        session=(client.session.save())
    print(session)
# session()

def is_photo(event):
    try:
        if(event.media.photo):
            return True
    except:
        return False

def is_document(event):
    try:
        if(event.media.document):
            return True
    except:
        return False

def is_link(event):
    try:
        if(event.media.webpage):
            return True
    except:
        return False

def forward():
    from_=list(from_channels.values())
    to_=list(to_channels.values())
    client = TelegramClient(StringSession(eval(profile)), api_id, api_hash)
    print("Bot Started")
    @client.on(events.NewMessage)
    async def handler(event):
        chat=await event.get_chat()
        chat_id=event.chat_id
        if(chat_id not in from_):
            return
        else:
            for j in others:
                s=''.join(event.text.lower())
                s=s.split(" ")
                for k in s:
                    if(j in k):
                        return

        for i in to_:
            try:
                if(event.poll):
                    return         
                elif(is_photo(event)):
                    try:
                        photo = event.media.photo                    
                        await client.send_file(i, photo, caption = event.text)
                    except:
                        await client.send_message(i, event.text)
                elif(is_document(event)):
                    media = event.media.document
                    await client.send_file(i, media, caption = event.text)
                else:
                    event.text=event.text+"\nFor more info visit-\nwww.socalledhappenings.in"                
                    await client.send_message(i, event.text,silent=False)
            except Exception as e:
                print(e)

    client.start()
    client.run_until_disconnected()
forward()
