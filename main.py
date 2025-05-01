# import telebot
# import os
# from dotenv import load_dotenv
# from src.bot_handlers import start, next_game, score, line
# from src.pandascore_api import PandaScoreAPI

# # Carrega as variáveis de ambiente
# load_dotenv()

# # Configuração do bot
# bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

# # Registra os handlers passando a instância do bot
# bot.message_handler(['start', 'help'])(lambda msg: start(bot, msg))
# bot.message_handler(['next_game'])(lambda msg: next_game(bot, msg))
# bot.message_handler(['score'])(lambda msg: score(bot, msg))
# bot.message_handler(['line'])(lambda msg: line(bot, msg))

# # Inicia o bot
# bot.infinity_polling()

import telebot
import os
from dotenv import load_dotenv
from flask import Flask, request

from src.bot_handlers import start, next_game, score, line
from src.pandascore_api import PandaScoreAPI

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')  # Defina essa variável no Render

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Registra os handlers
bot.message_handler(['start', 'help'])(lambda msg: start(bot, msg))
bot.message_handler(['next_game'])(lambda msg: next_game(bot, msg))
bot.message_handler(['score'])(lambda msg: score(bot, msg))
bot.message_handler(['line'])(lambda msg: line(bot, msg))

@app.route('/' + API_TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    return 'Bot está rodando!', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if WEBHOOK_URL:
        bot.remove_webhook()
        bot.set_webhook(url=f"{WEBHOOK_URL}/{API_TOKEN}")
    app.run(host='0.0.0.0', port=port)