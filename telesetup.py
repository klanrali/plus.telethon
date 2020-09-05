#Hello. These files are all private to Source Iraq Thun. 
#In short, there are files registered for Source, another group. 
#You do not need to write a file from the beginning for the sake of rights, 
#and there are complete files. Thank you for installing Iraq Thun. 
#Our channel is here: https://t.me/tele_thon

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
