from telegram import Bot
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def gui_tin():
    with open("bongda.jpg", "rb") as photo:
        await bot.send_photo(
            chat_id=CHAT_ID,
            photo=photo,
            caption="""🚨 Đang back mã rồi, anh em vào lưu và chốt đơn ngay!

🔥 Mã rất nhanh hết, ai chưa lưu tranh thủ vào ngay.

🔗 Lưu mã tại:
https://s.shopee.vn/3qLGV9WFVL
"""
        )

asyncio.run(gui_tin())
