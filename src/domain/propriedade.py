class Propriedade:
    def __init__(self, preco, aluguel) -> None:
        self._preco = preco
        self._aluguel = aluguel
        self._dono = None

    @property
    def preco(self) -> int:
        return self._preco
    
    @preco.setter
    def preco(self, value) -> None:
        self.preco = value

    @property
    def aluguel(self) -> int:
        return self._aluguel
    
    @aluguel.setter
    def aluguel(self, value) -> None:
        self._aluguel = value

    @property
    def dono(self) -> str:
        return self._dono
    
    @dono.setter
    def dono(self, value) -> None:
        self._dono = value
