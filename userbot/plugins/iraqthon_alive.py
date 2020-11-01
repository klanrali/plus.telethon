import time
from platform import python_version

from telethon import version

from userbot import ALIVE_NAME, CMD_HELP, StartTime, catdef, catversion

from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
CAT_IMG = Config.ALIVE_PIC


@borg.on(admin_cmd(outgoing=True, pattern="alive$"))
@borg.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    hmm = bot.uid
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if CAT_IMG:
        cat_caption = f"⌔︙🕷🇮🇶 IRAQTHON BOT\n"
        cat_caption += f"⌔︙🕷🇮🇶 Created By: [CH KLANR](https://t.me/RXXRX) || [CH IQ](https://t.me/IQTHON)\n"
        cat_caption += f"⌔︙🕷🇮🇶 Version: 1.0.1\n"
        cat_caption += (
            f"⌔︙🕷🇮🇶 The repo iraq: [Here](https://github.com/klanrali/iraq.thon)\n"
        )
        cat_caption += f"⌔︙🕷🇮🇶 Python Version : `{python_version()}\n`"
        cat_caption += f"⌔︙🕷🇮🇶 Uptime : `{uptime}\n`"
        cat_caption += f"⌔︙🕷🇮🇶 My Master: [{DEFAULTUSER}](tg://user?id={hmm})\n"
        await borg.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"⌔︙🕷🇮🇶 IRAQTHON BOT\n\n"
            f"⌔︙🕷🇮🇶 Created By: [CH KLANR](https://t.me/RXXRX) || [CH IQ](https://t.me/IQTHON)\n"
            f"⌔︙🕷🇮🇶 Version: 1.0.1\n"
            f"⌔︙🕷🇮🇶 The repo iraq: [Here](https://github.com/klanrali/iraq.thon)\n"
            f"⌔︙🕷🇮🇶 Python Version : `{python_version()}\n`"
            f"⌔︙🕷🇮🇶 Uptime : `{uptime}\n`"
            f"⌔︙🕷🇮🇶 My Master: [{DEFAULTUSER}](tg://user?id={hmm})\n",
        )


@borg.on(admin_cmd(outgoing=True, pattern="cugialivenk$"))
@borg.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
    reply_to_id = alive.message
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    hmm = bot.uid
    cat_caption = f"**Catuserbot is Up and Running**\n"
    cat_caption += f"**  -Telethon Version :** `{version.__version__}\n`"
    cat_caption += f"**  -Catuserbot Version :** `{catversion}`\n"
    cat_caption += f"**  -Python Version :** `{python_version()}\n`"
    cat_caption += f"**  -My Peru Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Var.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** `alive`\
      \n\n**Syntax : **`.alive` \
      \n**Usage : ** status of bot.\
      \n\n**Syntax : **`.ialive` \
      \n**Usage : ** inline alive."
    }
)
