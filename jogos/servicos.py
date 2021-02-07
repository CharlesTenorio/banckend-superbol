from servicos.service import LerDadosAPI
from datetime import datetime
from ligas.models import Liga
from .models import jogo


def Incluir_jogos_novos():
    jogos = LerDadosAPI()
    lista_liga = Liga.objects.all()
    
    for liga in lista_liga:
         result = jogos.lista_jogos('Novos', str(liga.id))
         if result:
             for res in result:
                 partida = jogo.objects.create(id_partida=res["id"], id_time_casa[""])



    



