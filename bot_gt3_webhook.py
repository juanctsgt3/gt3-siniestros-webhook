import os
import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from datetime import datetime
import schedule
import time

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
USER_ID = int(os.getenv("USER_ID"))

BOT = Bot(token=BOT_TOKEN)

# Aquí pondrías las funciones para scrapear las 11 webs, ahora sólo simula
def buscar_gt3_siniestros():
    resultado = (
        "<b>Resumen diario GT3 siniestrados:</b>\n"
        "1. <a href='https://www.copart.com/lotSearchResults?free=true&query=porsche%20911%20gt3'>Copart</a>\n"
        "2. <a href='https://plc.auction/es/auction/from-de/porsche/911'>PLC Auction</a>\n"
        "3. <a href='https://www.autoscout24.es/lst/porsche/992/ve_gt3'>Autoscout24</a>\n"
        "4. <a href='https://www.iaai.com/Search'>IAAI General</a>\n"
        "5. <a href='https://www.iaai.com/VehicleDetail/42512601~US'>IAAI Lote específico</a>\n"
        "6. <a href='https://www.salvagemarket.co.uk/Search?searchText=porsche%20911'>Salvage Market</a>\n"
        "7. <a href='https://m.mobile.de/auto/search.html?cn=DE&dam=true&ms=20100%3B28%3B%3B&od=up'>Mobile.de</a>\n"
        "8. <a href='https://abetter.bid/en/car-finder/model-911/year-2013-2025?search_query=Porsche+911+'>A Better Bid</a>\n"
        "9. <a href='https://carsfromwest.com'>Cars from West</a>\n"
        "10. <a href='https://www.dubizzle.com'>Dubizzle</a>\n"
        "11. <a href='https://www.autodna.com'>AutoDNA</a>"
    )
    return resultado

async def enviar_resumen_diario():
    texto = buscar_gt3_siniestros()
    await BOT.send_message(chat_id=USER_ID, text=texto, parse_mode=ParseMode.HTML)

def tarea_diaria():
    asyncio.run(enviar_resumen_diario())

def main():
    tarea_diaria()
    schedule.every().day.at("08:00").do(tarea_diaria)
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
