from src.domain.propriedade import Propriedade


class Jogador:
    def __init__(self, nome, estrategia) -> None:
        self.nome = nome
        self.estrategia = estrategia
        self.saldo = 300
        self.posicao = 0
        self.ativo = True
        self.propriedades = []

    def mover(self, dado, tabuleiro) -> None:
        self.posicao = (self.posicao + dado) % len(tabuleiro)
        if self.posicao + dado >= len(tabuleiro):
            self.saldo += 100

    def comprar(self, propriedade: Propriedade) -> None:
        if propriedade.dono is None and self.saldo >= propriedade.preco:
            if self.estrategia:
                self.saldo -= propriedade.preco
                propriedade.dono = self
                self.propriedades.append(propriedade)

    def pagar_aluguel(self, propriedade: Propriedade) -> None:
        if propriedade.dono and propriedade.dono != self:
            self.saldo -= propriedade.aluguel
            propriedade.dono.saldo += propriedade.aluguel
            