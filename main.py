import telebot
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Configuração do bot
bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

import requests
import os
from dotenv import load_dotenv

load_dotenv()

class PandaScoreAPI:
    def __init__(self):
        self.token = os.getenv('PANDASCORE_TOKEN')
        self.base_url = 'https://api.pandascore.co'
        self.headers = {
            'Authorization': f'Bearer {self.token}'
        }

    def _make_request(self, endpoint):
        url = f'{self.base_url}{endpoint}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return None

    def get_upcoming_matches(self, team_slug='furia', game='csgo'):
        #Obtém os próximos jogos do jogo especificado
        return self._make_request(f'/{game}/matches/upcoming?filter[opponent_id]={team_slug}') 

    def get_live_matches(self, team_slug='furia', game='csgo'):
        """Obtém os jogos ao vivo do jogo especificado"""
        return self._make_request(f'/{game}/matches/running?filter[opponent_id]={team_slug}')

    def get_match_details(self, match_id, game='csgo'):
        """Obtém detalhes específicos de um jogo"""
        return self._make_request(f'/{game}/matches/running?filter[id]={match_id}')

    def get_team_players(self, team_name='FURIA', game='csgo'):
        """Obtém os jogadores de um time específico"""
        return self._make_request(f'/{game}/teams?filter[name]={team_name}') 

@bot.message_handler(['start', 'help'])
def start(msg):
    bot.reply_to(msg, """
                 🔥Olá Furioso!🔥\n\n Aqui estão alguns comandos para você ficar por dentro de TUDO sobre a nossa querida FÚRIA! 🇧🇷🎮\n\n📋/help -> Instruções e comandos disponíveis 🤔\n\n🗓️/next_game -> Quando rolam os próximos jogos da FÚRIA! ⏰\n\n🏆/score -> Placares ao vivo dos jogos atuais! 📊\n\n👥/line -> Quem são os guerreiros na line principal do time! 💪
                 """)
    

@bot.message_handler(['next_game'])
def next_game(msg):
        panda_api = PandaScoreAPI()
        matches = panda_api.get_upcoming_matches()
        if matches:
            response = "Próximos jogos da Fúria:\n\n"
            for match in matches[:5]:  # Mostra os 5 próximos jogos
                response += f"🏆 {match['league']['name']}\n"
                if len(match['opponents']) >= 2:
                    response += f"🆚 {match['opponents'][0]['opponent']['name']} vs {match['opponents'][1]['opponent']['name']}\n"
                else:
                    response += "🆚 Times ainda não definidos\n"
                response += f"⏰ {match['scheduled_at']}\n\n"
        else:
            response = """😔 No momento não temos jogos da FÚRIA marcados no calendário.\n\n⏳ Mas não se preocupe! Logo teremos novos desafios para nossa equipe!\n\n🔄 Use o comando /next_game regularmente para ser o primeiro a saber quando os próximos jogos forem agendados.\n\n💪 Enquanto isso, continue acompanhando as redes sociais da FÚRIA para novidades e conteúdos exclusivos!\n\nPara voltar ao menu principal use o comando 📋/help"""
        
        bot.reply_to(msg, response)

@bot.message_handler(['score'])
def score(msg):
        panda_api = PandaScoreAPI()
        matches = panda_api.get_live_matches()
        if matches:
            response = "Jogos ao vivo:\n\n"
            for match in matches:
                response += f"🏆 {match['league']['name']}\n"
                if len(match['opponents']) >= 2:
                    response += f"🆚 {match['opponents'][0]['opponent']['name']} {match['results'][0]['score']} x {match['results'][1]['score']} {match['opponents'][1]['opponent']['name']}\n"
                else:
                    response += "🆚 Times ainda não definidos\n"
                response += f"⏰ {match['status']}\n\n"
        else:
            response = """📺 No momento não temos nenhum jogo da FÚRIA ao vivo. 😭\n\n⏰ Fique de olho nas nossas atualizações e redes sociais para novidades e conteúdos exclusivos!\n\nPara voltar ao menu principal use o comando 📋/help"""
        
        bot.reply_to(msg, response)

@bot.message_handler(['line'])
def line(msg):
    panda_api = PandaScoreAPI()
    team_data = panda_api.get_team_players()
    
    if team_data and isinstance(team_data, list) and len(team_data) > 0:
        # Normalmente, a API retorna um time com seus jogadores
        if 'players' in team_data[0]:
            players = team_data[0]['players']
            response = "🔥 Time atual da FURIA:\n\n"
            
            for player in players:
                if 'name' in player:
                    nickname = player.get('name', 'Desconhecido')
                    first_name = player.get('first_name', '')
                    last_name = player.get('last_name', '')
                    full_name = f"{first_name} '{nickname}' {last_name}".strip()
                    response += f"👾 {full_name}\n"
            response += "\nPara voltar ao menu principal use o comando 📋/help"
            
            bot.reply_to(msg, response)
        else:
            bot.reply_to(msg, "Não foi possível encontrar os jogadores do time FURIA.\n\nPara voltar ao menu principal use o comando 📋/help")
    else:
        bot.reply_to(msg, "Não foi possível obter informações sobre o time FURIA no momento.\n\nPara voltar ao menu principal use o comando 📋/help")     

# Inicia o bot
bot.infinity_polling()