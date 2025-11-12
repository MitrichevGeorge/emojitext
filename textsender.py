import os
import asyncio
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import MessageEntityType
from pyrogram.types import MessageEntity

load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

app = Client("my_userbot", api_id=API_ID, api_hash=API_HASH)

prids = {
    'а': 5197622108535949952,
    'б': 5199793854454202534,
    'в': 5199427188801176651,
    'г': 5199785586642168479,
    'д': 5197286581395816962,
    'е': 5199797307607908627,
    'ё': 5197479438312308798,
    'ж': 5199552202414263222,
    'з': 5199700331541332780,
    'и': 5199557291950507324,
    'й': 5197463937775339374,
    'к': 5199536341100039541,
    'л': 5199624946275352981,
    'м': 5197392117332213267,
    'н': 5197183570900191145,
    'о': 5197160403846598276,
    'п': 5199497286962414953,
    'р': 5197255666221222531,
    'с': 5197319339111383487,
    'т': 5197196189514106271,
    'у': 5197430454210298439,
    'ф': 5199890529873071504,
    'х': 5199840583698384073,
    'ц': 5199564395826415329,
}

async def send_text(s):
    """Отправляет текст кастомными эмодзи"""
    if not app.is_connected:
        await app.start()
    
    entities = []
    text = ""
    
    for i, char in enumerate(s.lower()):
        if char in prids:
            text += "⭐"
            entities.append(
                MessageEntity(
                    type=MessageEntityType.CUSTOM_EMOJI,
                    offset=i,
                    length=1,
                    custom_emoji_id=prids[char]
                ))
        else:
            text += char
    
    await app.send_message("me", text, entities=entities)

async def main():
    """Пример использования"""
    await send_text("привет")

async def stop_app():
    """Корректное завершение"""
    try:
        await app.stop()
    except RuntimeError as e:
        if "attached to a different loop" not in str(e):
            raise

if __name__ == "__main__":
    asyncio.run(main())
