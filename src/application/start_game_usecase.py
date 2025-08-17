import random
from typing import List
from pydantic import BaseModel
from src.domain.game import Game
from src.domain.strategies import Strategies


class Output(BaseModel):
    vencedor: str
    jogadores: List[str]

class StartGameUsecase:
    def __init__(self) -> None:
        self._strategies = Strategies()
        self._game = Game(self._strategies.generate())
        self._jogadores = self._game.jogadores
        self._rodada = 0

    async def execute(self)  -> Output:
        while self._rodada < 100 and sum(j.ativo for j in self._jogadores) > 1:
            for jogador in self._jogadores:
                if not jogador.ativo:
                    continue
                dado = random.randint(1, 6)
                self._game.play(jogador, dado)
            self._rodada += 1
        self._game.jogadores.sort(key=lambda j: j.saldo, reverse=True)
        return Output(vencedor=self._game.jogadores[0].nome, jogadores=[j.nome for j in self._game.jogadores])
        
