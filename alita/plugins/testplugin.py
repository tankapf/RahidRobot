# Copyright (C) 2020 - 2021 Divkix. All rights reserved. Source code available under the AGPL.
#
# This file is part of Alita_Robot.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
from time import time
from random import choice
from pyrogram.types import Message

from alita.bot_class import Alita
from alita.utils.custom_filters import command

photolist = [
"https://telegra.ph/file/8e62602ac8201d8849875.jpg",
"https://telegra.ph/file/db96a3aeccdd9fc96aed6.jpg",
"https://telegra.ph/file/976eb502056dfe335a283.jpg",
"https://telegra.ph/file/bbd51ccf0a2401ef09eda.jpg",
"https://telegra.ph/file/a09c109ce8ea562311c0c.jpg",
]

@Alita.on_message(command("alive", sudo_cmd=False))
async def test_bot(bot: Alita, m: Message):
    start = time()
    replymsg = await m.reply_text("❤️ Hesablanır...")
    end = round(time() - start, 2)
    photo = random.choice(photolist)
    text = f"❤️ **Haycan, Mən işləyirəm**\n👨🏻‍💻 **Sahib [HÜSEYN](http://t.me/HuseynH\n️📣 **Kanal -**[NeBaxsan](http://t.me/HoneyBeestChannel\n👥 **Söhbət Qrupu -**@7172501878ffd261a9f78.mp4\nℹ️ __Bunu yazmağım {end} saniyə çəkdi__"
    await bot.send_photo(m.chat.id, photo=photo, caption=text)
