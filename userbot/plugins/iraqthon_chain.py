#Hello. These files are all private to Source Iraq Thun. 
#In short, there are files registered for Source, another group. 
#You do not need to write a file from the beginning for the sake of rights, 
#and there are complete files. Thank you for installing Iraq Thun. 
#Our channel is here: https://t.me/tele_thon
from .. import CMD_HELP
from telethon import events
from ..utils import admin_cmd, sudo_cmd, edit_or_reply
from telethon.tl.functions.messages import SaveDraftRequest

@borg.on(admin_cmd(pattern="chain$"))
@borg.on(sudo_cmd(pattern="chain$",allow_sudo = True))
async def _(event):
    await event.edit("Counting...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await borg(SaveDraftRequest(
                await event.get_input_chat(),
                "",
                reply_to_msg_id=message.id
            ))
        message = reply
        count += 1
    await event.edit(f"Chain length: {count}")
    
CMD_HELP.update({
    "chain":
    "**SYNTAX :** `.chain`\
    \n**USAGE : **Reply this command to any converstion where you want to find length of converstion(Only tagged chain will count ) \
    "
})
