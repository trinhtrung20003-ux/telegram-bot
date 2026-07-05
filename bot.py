from telegram import Bot
import asyncio

# Token bot Telegram
TOKEN = "8026861100:AAEoy8Si4uVkud-OmVPU9uWNYH_hcIj80EM"

# Kênh Telegram
CHAT_ID = "@sanpcshopee"

bot = Bot(token=TOKEN)

async def gui_tin():
    with open("anh.jpg.png", "rb") as photo:
        await bot.send_photo(
            chat_id=CHAT_ID,
            photo=photo,
            caption="""📌 Đang back mã Shopee 100K/0đ SVIP

Lưu tại:
https://s.shopee.vn/20tWm6nM5Q"""
        )

asyncio.run(gui_tin())
