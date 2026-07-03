from telegram import Bot
import asyncio

TOKEN = "8026861100:AAEoy8Si4uVkud-OmVPU9uWNYH_hcIj80EM"
CHAT_ID = "6086572676"

bot = Bot(token=TOKEN)

async def gui_tin():
    with open("anh.jpg.jfif", "rb") as photo:
        await bot.send_photo(
            chat_id=CHAT_ID,
            photo=photo,
            caption="caption="""📌 Đang back mã Shopee 100K/0đ SVIP

Lưu tại:
https://s.shopee.vn/20tWm6nM5Q""""
        )

asyncio.run(gui_tin())
