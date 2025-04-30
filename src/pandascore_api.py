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