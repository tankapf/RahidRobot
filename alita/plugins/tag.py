# Bu plugin aykhan_s tərəfindən yaradılıb !
# Kopyalayan dəyişdirən pe*sərdi...!!!
# t.me/aykhan_s | t.me/RoBotlarimTg

from telethon.tl.types import ChannelParticipantsAdmins
from EmmaMiller.events import register as aykhan

@aykhan(pattern="^/tag")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tag"
    chat = await event.get_input_chat()
    leng = 0
    async for x in bot.iter_participants(chat):
        if leng < 4092:
            mentions += f"[\u2063](tg://user?id={x.id})"
            leng += 1
    await event.reply(mentions)
    await event.delete()

__help__ = """
Modul Sahibi - @aykhan_s 
 ❍ /tag: İstifadəçiləri tağ edər
"""
__mod_name__ = "🖇️Tağ"