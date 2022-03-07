import secrets
import string
import aiohttp
from pyrogram import filters
from cryptography.fernet import Fernet
from alita.tr_engine import tlang
from alita.bot_class import Alita as Nezrin
from Nezrin.komekci import tes_zarafat


@Nezrin.on_message(filters.command("/zarafat") & ~filters.edited)
async def commit(_, message):
    await message.reply_text((await tes_cavab('Nezrin/txt/zarafat.txt')))

__PLUGIN__ = "zarafat"
_DISABLE_CMDS_ = [
    "zarafat",
]
