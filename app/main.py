import os
import requests
from fastapi import FastAPI, Request
from telegram import Bot
from loguru import logger

# Inicializar FastAPI
app = FastAPI()

# Configuración del bot de Telegram
TOKEN = '7726295961:AAFeWvujqB2B4B-K-0e0nwb2mPwWY6CHifY'
bot = Bot(token=TOKEN)

# Configuración de Loguru para registrar accesos y mensajes
logger.add("app_logs.log", rotation="1 MB", retention="10 days", level="DEBUG")

# Endpoint de bienvenida
@app.get("/")
def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to BOLSAPI: the crypto and commodities alert bot API!"}

# Webhook de Telegram
@app.post("/webhook")
async def webhook(request: Request):
    update = await request.json()
    logger.info(f"Update recibido: {update}")  # Registrar el update recibido

    chat_id = update['message']['chat']['id']
    message_text = update['message']['text']

    # Responder al mensaje
    await bot.send_message(chat_id=chat_id, text="¡Hola! Tu mensaje fue recibido.")

    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

