from celery import shared_task
from servicos.service import LerDadosAPI, urls
from .models import Liga

@shared_task
def incluir_ligas():
    salvar = False
    try:
        
      qtd_ligas = Liga.objects.count()
      if qtd_ligas <= 0:
        obj_ligas = LerDadosAPI()
        l = urls["ligas"]+"1"
        qtd_pg = int(obj_ligas.qtd_paginas_registros(l))
        for i in range(qtd_pg):
            ligas = obj_ligas.listar_ligas(i)
            if ligas:
              for liga in ligas["results"]:
                  lg = Liga(id=liga['id'],
                     nome=liga['name'],
                     cc=liga['cc'],
                     has_leaguetable=liga["has_leaguetable"],
                     has_toplist=liga["has_toplist"])
                     

                  lg.save()
                 
              salvar=True         
    except Exception as e:
        print(str(e))
        salvar=False
    return salvar    

