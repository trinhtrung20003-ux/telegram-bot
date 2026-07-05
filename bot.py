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
            caption="""📌 Đang back lượt mã SVIP 40% - Giảm tối đa 100K/0đ dùng ngay

► Lưu tại: https://s.shopee.vn/2qSjEc49TM

⚠ Lưu ý:
► Đối với ai đã lưu mã trước đó, sau khi thấy thông báo back bấm mở liên tục mục Shopee Voucher cho tới khi thấy mã 40% hiện, chọn và đặt hàng nhanh.

► Đối với ai chưa lưu, canh trước khung giờ back mã hoặc sau khi có thông báo back mã thì load lại liên tục từ 0–2 phút. Sau khi lưu được thì vào mua nhanh. Nếu hết mã thì chờ lần back sau và làm theo cách đã lưu trước đó.

Lưu tại:
https://s.shopee.vn/20tWm6nM5Q"""
        )

asyncio.run(gui_tin())
