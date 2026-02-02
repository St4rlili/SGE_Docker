# bot_socios.py
import requests, os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")  # Token BotFather
API_URL = os.getenv("API_URL")  # API REST

# Funciones para interactuar con la API REST

def crear_socio(data):
    response = requests.post(API_URL, json=data)
    return response.json(), response.status_code

def modificar_socio(data):
    response = requests.put(API_URL, json=data)
    return response.json(), response.status_code

def consultar_socio(num_socio):
    payload = {"data": f'{{"num_socio": {num_socio}}}'}
    response = requests.get(API_URL, params=payload)
    return response.json(), response.status_code

def borrar_socio(num_socio):
    payload = {"data": f'{{"num_socio": {num_socio}}}'}
    response = requests.delete(API_URL, params=payload)
    return response.json(), response.status_code

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.strip()
    chat_id = update.message.chat_id

    # Crear socio: Crear nombre=xxxx,apellidos=xxxx,num_socio=x
    if texto.lower().startswith("crear"):
        try:
            params = texto[6:]
            data = {k.strip(): int(v) if k.strip() == "num_socio" else v.strip()
                    for k, v in (x.split("=") for x in params.split(","))}
            res, status = crear_socio(data)
            await context.bot.send_message(chat_id, f"Respuesta Crear ({status}): {res}")
        except Exception as e:
            await context.bot.send_message(chat_id, f"Error al crear: {e}")
        return

    # Modificar socio: Modificar nombre=xxxx,apellidos=xxxx,num_socio=x
    elif texto.lower().startswith("modificar"):
        try:
            params = texto[10:]
            data = {k.strip(): int(v) if k.strip() == "num_socio" else v.strip()
                    for k, v in (x.split("=") for x in params.split(","))}
            res, status = modificar_socio(data)
            await context.bot.send_message(chat_id, f"Respuesta Modificar ({status}): {res}")
        except Exception as e:
            await context.bot.send_message(chat_id, f"Error al modificar: {e}")
        return

    # Consultar socio: Consultar num_socio=x
    elif texto.lower().startswith("consultar"):
        try:
            params = texto[9:]
            num_socio = int(params.split("=")[1])
            res, status = consultar_socio(num_socio)
            await context.bot.send_message(chat_id, f"Respuesta Consultar ({status}): {res}")
        except Exception as e:
            await context.bot.send_message(chat_id, f"Error al consultar: {e}")
        return

    # Borrar socio: Borrar num_socio=x
    elif texto.lower().startswith("borrar"):
        try:
            params = texto[7:]
            num_socio = int(params.split("=")[1])
            res, status = borrar_socio(num_socio)
            await context.bot.send_message(chat_id, f"Respuesta Borrar ({status}): {res}")
        except Exception as e:
            await context.bot.send_message(chat_id, f"Error al borrar: {e}")
        return

    else:
        await context.bot.send_message(chat_id, "Orden no soportada")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))
    print("Bot de socios iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
