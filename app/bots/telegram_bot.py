from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from app.services import get_bitcoin_price, get_gold_price, get_silver_price
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger
import time

# Configuración para guardar los logs en un archivo
logger.add("app_logs.log", rotation="1 MB", retention="10 days", level="DEBUG")

# Un mensaje simple para verificar que Loguru está funcionando
logger.info("Bot de Telegram iniciado correctamente")

# Inicializa un valor de precios antiguos
previous_prices = {
    'bitcoin': 0,
    'gold': 0,
    'silver': 0
}

# Función que envía las alertas si los precios cambian significativamente
async def check_price_changes(context: ContextTypes.DEFAULT_TYPE):
    global previous_prices

    # Obtenemos los precios actuales
    new_bitcoin_price = get_bitcoin_price()
    new_gold_price = get_gold_price()
    new_silver_price = get_silver_price()

    # Comparar con los precios anteriores y enviar alertas si el cambio es significativo
    if abs(new_bitcoin_price - previous_prices['bitcoin']) > 500:  # Cambio significativo de $500
        await context.bot.send_message(chat_id='YOUR_CHAT_ID', text=f"Alerta: El precio de Bitcoin ha cambiado a ${new_bitcoin_price}")
        previous_prices['bitcoin'] = new_bitcoin_price

    if abs(new_gold_price - previous_prices['gold']) > 50:  # Cambio significativo de $50 en oro
        await context.bot.send_message(chat_id='YOUR_CHAT_ID', text=f"Alerta: El precio del Oro ha cambiado a ${new_gold_price}")
        previous_prices['gold'] = new_gold_price

    if abs(new_silver_price - previous_prices['silver']) > 5:  # Cambio significativo de $5 en plata
        await context.bot.send_message(chat_id='YOUR_CHAT_ID', text=f"Alerta: El precio de la Plata ha cambiado a ${new_silver_price}")
        previous_prices['silver'] = new_silver_price

# Función para mostrar precios al usuario (cuando lo solicite)
async def show_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bitcoin_price = get_bitcoin_price()
    gold_price = get_gold_price()
    silver_price = get_silver_price()

    message = (f"Precios actuales:\n"
               f"Bitcoin: ${bitcoin_price}\n"
               f"Oro: ${gold_price} USD\n"
               f"Plata: ${silver_price} USD")

    await update.message.reply_text(message)

# Inicializa el bot y los handlers
def main():
    # Reemplaza 'YOUR TELEGRAM TOKEN' por tu token de BotFather
    application = ApplicationBuilder().token('7726295961:AAFeWvujqB2B4B-K-0e0nwb2mPwWY6CHifY').build()

    # Reemplaza 'YOUR_CHAT_ID' por tu chat ID personal o del grupo donde enviarás las alertas
    application.add_handler(CommandHandler("start", show_prices))
    application.add_handler(CommandHandler("prices", show_prices))

    # Inicializa un scheduler para las alertas periódicas
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: application.job_queue.run_once(check_price_changes, when=1), 'interval', minutes=10)
    scheduler.start()

    # Corre el bot en modo polling
    application.run_polling()

if __name__ == "__main__":
    main()


