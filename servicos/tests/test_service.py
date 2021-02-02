from servicos.service import LerDadosAPI


def test_lista_times():
    time = LerDadosAPI()
    codigo= time.lista_times()
   
    assert codigo.status_code == 200

def test_lista_ligas():
    liga = LerDadosAPI()
    codigo = liga.lista_ligas()
    assert codigo.status_code== 200


def test_lista_ligas_tbl():
    liga = LerDadosAPI()
    codigo = liga.lista_ligas_tabela(155)
    assert codigo.status_code== 200

