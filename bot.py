from telegram import Bot
import asyncio
import schedule
import time

TOKEN = "8026861100:AAEoy8Si4uVkud-OmVPU9uWNYH_hcIj80EM"
CHAT_ID = "6086572676"

bot = Bot(token=TOKEN)

async def gui_tin():
  with open(r"C:\Users\skyce\Desktop\59f4fc82-8b52-42a6-9090-fd9e5f1450be (1).jfif", "rb") as photo:
        await bot.send_photo(
            chat_id=6086572676,
            photo=photo,
            caption="""📌 Đang back mã Shopee 100K/0đ SVIP

Lưu tại:
https://s.shopee.vn/20tWm6nM5Q"""
        )


def job():
    asyncio.run(gui_tin())

# Các giờ gửi
schedule.every().day.at("00:01").do(job)
schedule.every().day.at("09:00").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("20:00").do(job)

print("Bot đang chạy...")

while True:
       schedule.run_pending()
       time.sleep(1)
