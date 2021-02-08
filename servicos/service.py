from dataclasses import dataclass
import requests
from decouple import config
from datetime import datetime



@dataclass(init=True, frozen=True)
class LerDadosAPI:
    token:str = 'token='+config("API_TOKEN")
    url_base_v1:str = config("BASE_URL_V1")
    url_base_v2:str = config("BASE_URL_V2")
    time : str = "team"
    sport: str = "1"# tutebol e 1
   
    def listar_times(self):
        url_time = self.url_base_v1+self.time+'?'+self.token+'&sport_id='+self.sport
        r = requests.get(url_time)
        return r.json()

    def listar_ligas(self):
        url_liga = self.url_base_v1+'league?'+self.token+'&sport_id='+self.sport
        r= requests.get(url_liga)
        return r.json()

    def listar_ligas_tabela(self, id_liga):
       
        url_liga_tlb = self.url_base_v2+'league/table?'+self.token+'&league_id='+str(id_liga)
        r= requests.get(url_liga_tlb)
        return r.json()    
    
    def listar_jogos(self, tipo_jogo, league_id):
        url_jogos = ''
        if tipo_jogo == 'Marcado':
            url_jogos = self.url_base_v2+'events/upcoming?sport_id='+self.sport+'&league_id='+league_id+'&'+self.token
           
        else:
            url_jogos=self.url_base_v2+'events/ended?sport_id='+self.sport+'&league_id='+league_id+'&'+self.token

        r= requests.get(url_jogos)
        return r.json()      
                