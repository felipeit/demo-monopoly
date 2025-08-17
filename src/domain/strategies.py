import random
from src.domain.jogador import Jogador


class Strategies:
    def impulsivo(self) -> bool:
        return random.choice([True, False])

    def exigente(self) -> bool:
        return random.choice([True, False])

    def cauteloso(self) -> bool:
        return random.choice([True, False])

    def aleatorio(self) -> bool:
        return random.choice([True, False])
    
    def generate(self) -> list[Jogador]:
        jogadores = [
            Jogador("impulsivo", self.impulsivo()),
            Jogador("exigente", self.exigente()),
            Jogador("cauteloso", self.cauteloso()),
            Jogador("aleatorio", self.aleatorio())
        ]
        random.shuffle(jogadores)
        return jogadores