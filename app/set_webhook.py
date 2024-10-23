import requests

TOKEN = '7726295961:AAFeWvujqB2B4B-K-0e0nwb2mPwWY6CHifY'  # Reemplaza por tu token de bot
WEBHOOK_URL = 'https://tu-aplicacion.vercel.app/webhook'  # Cambia esto a la URL de tu aplicación en Vercel

# Establecer el webhook
response = requests.post(f'https://api.telegram.org/bot{TOKEN}/setWebhook', data={'url': WEBHOOK_URL})

print(response.json())  # Verifica la respuesta
