from unittest.mock import Mock


def test_lista_jogos():
    jogo = Mock(return_valeu=200)
    codigo= jogo.return_valeu
    assert codigo == 200
