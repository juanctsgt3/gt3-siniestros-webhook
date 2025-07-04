
from telegram import Bot
from telegram.constants import ParseMode
import asyncio
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
USER_ID = int(os.getenv("USER_ID"))

BOT = Bot(token=TELEGRAM_TOKEN)

async def send_daily_summary():
    texto = """Resumen diario GT3 siniestrados:

1. Copart: https://www.copart.com/lotSearchResults
2. PLC Auction: https://plc.auction/es/auction/from-de/porsche/911
3. AutoScout24: https://www.autoscout24.es/lst/porsche/992/ve_gt3?atype=C&cy=D%2CA%2CB%2CE%2CF%2CI%2CL%2CNL&desc=0&powertype=kw&search_id=1qnsjfh2yjo&sort=standard&ustate=A
4. IAAI: https://www.iaai.com/Search?url=fWKBIzm5vlJ9CQqZKqq7rtcwGIzX5ILavqfA30taAYA%3d
5. Salvage Market: https://www.salvagemarket.co.uk/Search?searchText=porsche%20911

👉 Avisa si ves alguno interesante o pendiente.
"""

    await BOT.send_message(chat_id=USER_ID, text=texto, parse_mode=ParseMode.HTML)

if __name__ == "__main__":
    asyncio.run(send_daily_summary())
