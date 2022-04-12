## Github : @riz4d
## InstaGram : @riz.4d
# ______________________

import os
from pyrogram import Client, filters


DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

riz4d = Client(
    "Convert2Audio-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/rizad/")


@riz4d.on_message(filters.private & filters.text)
async def start(bot, message):
    await message.reply_text("""Hey Dude 🙋🏻!!
  I'm Convert2Audio bot
  Developed by @riz4d
  Sent me a video for convert to audio""")


@riz4d.on_message(filters.video & filters.private)
async def mp3(bot, message):
    
    # download video
    file_path = DOWNLOAD_LOCATION + f"{message.from_user.id}.mp3"
    txt = await message.reply_text("`Uploading to server ⌛️...`")
    await message.download(file_path)
    await txt.edit_text("`Uploaded Successfully ✅`")
    
    # convert to audio
    await txt.edit_text("`Converting to audio⌛️`")
    await message.reply_audio(audio=file_path, caption="Queries: @riz4d", quote=True)
    
    # remove file
    try:
        os.remove(file_path)
    except:
        pass
    
    await txt.delete()


riz4d.run()
