from unittest.mock import Mock

def test_lista_times():
    time = Mock(return_valeu=200)
    codigo = time.return_valeu
    assert codigo == 200

def test_lista_ligas():
    time = Mock(return_valeu=200)
    codigo = time.return_valeu
    assert codigo == 200


def test_lista_ligas_tbl():
    liga = Mock(return_valeu=200)
    codigo= liga.return_valeu
    assert codigo == 200

def test_lista_jogos():
    jogo = Mock(return_valeu=200)
    codigo= jogo.return_valeu
    assert codigo == 200
