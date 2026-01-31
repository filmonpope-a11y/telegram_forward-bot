from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
import os

# ========= CONFIG =========
api_id = int(os.getenv("API_ID", 20976878))
api_hash = os.getenv("API_HASH", "9ee80f7e691a8fbbec88fe79658e64fc")

session_name = "forward_session"

# Source & Target Channel IDs
source_id = -1001076711287   # SOURCE private/public channel
target_id = -1002954357757   # TARGET private/public channel
# ==========================

client = TelegramClient(session_name, api_id, api_hash)


@client.on(events.NewMessage(chats=source_id))
async def forward_new_message(event):
    msg = event.message

    try:
        # 🖼 Photo
        if msg.photo:
            await client.send_file(
                target_id,
                msg.photo,
                caption=msg.text or ""
            )

        # 📎 Document / Video / Audio
        elif msg.document:
            await client.send_file(
                target_id,
                msg.document,
                caption=msg.text or ""
            )

        # 📝 Text only
        else:
            if msg.text:
                await client.send_message(
                    target_id,
                    msg.text
                )

        print("✅ New message copied")

    except Exception as e:
        print("❌ Error:", e)


def main():
    print("🚀 Forward bot started (sender hidden, caption kept)")
    client.start()
    client.run_until_disconnected()


if name == "main":
    main()