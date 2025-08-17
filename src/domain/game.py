import random
from src.domain.jogador import Jogador
from src.domain.propriedade import Propriedade


class Game:
    def __init__(self, jogadores: list[Jogador]) -> None:
        self._tabuleiro = self._criar_tabuleiro()
        self._jogadores = jogadores

    def _criar_tabuleiro(self) -> list[Propriedade]:
        return [Propriedade(random.randint(50, 200), random.randint(10, 100)) for _ in range(20)]

    @property
    def jogadores(self) -> list[Jogador]:
        return self._jogadores
    
    @property
    def tabuleiro(self) -> list[Propriedade]:
        return self._tabuleiro

    def mover_jogador(self, jogador: Jogador, dado: int) -> None:
        jogador.posicao = (jogador.posicao + dado) % len(self._tabuleiro)
        if jogador.posicao + dado >= len(self._tabuleiro):
            jogador.saldo += 100

    def comprar_ou_pagar(self, jogador: Jogador) -> None:
        prop = self._tabuleiro[jogador.posicao]
        if prop.dono is None:
            jogador.comprar(prop)
        else:
            jogador.pagar_aluguel(prop)

    def verificar_saldo(self, jogador: Jogador) -> None:
        if jogador.saldo < 0:
            jogador.ativo = False
            for p in jogador.propriedades:
                p.dono = None
            jogador.propriedades.clear()

    def play(self, jogador: Jogador, dado: int) -> None:
        self.mover_jogador(jogador, dado)
        self.comprar_ou_pagar(jogador)
        self.verificar_saldo(jogador)