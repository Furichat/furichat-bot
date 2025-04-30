# main.py
import telebot
import os
from dotenv import load_dotenv
from src.bot_handlers import start, next_game, score, line
from src.pandascore_api import PandaScoreAPI

# Carrega as variáveis de ambiente
load_dotenv()

# Configuração do bot
bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

# Registra os handlers passando a instância do bot
bot.message_handler(['start', 'help'])(lambda msg: start(bot, msg))
bot.message_handler(['next_game'])(lambda msg: next_game(bot, msg))
bot.message_handler(['score'])(lambda msg: score(bot, msg))
bot.message_handler(['line'])(lambda msg: line(bot, msg))

# Inicia o bot
bot.infinity_polling()