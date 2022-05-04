#@Aadhi000 #AVR

import os
import math
import time
import heroku3
import requests
from pyrogram import Client, filters
from info import COMMAND_HAND_LER

#=====================================================
BOT_START_TIME = time.time()

HEROKU_API_KEY = (os.environ.get("HEROKU_API_KEY", ""))
#=====================================================

@Client.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()  
    avr = await message.reply_text("•••")  
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%Hh | %Mm | %Ss", time.gmtime(time.time() - BOT_START_TIME))   
    await avr.edit(f"-ᴄᴜʀʀᴇɴᴛ ʙᴏᴛ sᴛᴀᴛᴜs-\n\n‹› 🏓 ᴘᴏɴɢ : {time_taken_s:.3f} ms\n‹› ⏰ ᴜᴘᴛɪᴍᴇ : {uptime}")
