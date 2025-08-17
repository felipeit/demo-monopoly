from typing import List

from pydantic import BaseModel
from src.application.start_game_usecase import StartGameUsecase
from fastapi import FastAPI

app = FastAPI()
class Response(BaseModel):
    vencedor: str
    jogadores: List[str]

@app.post("/jogo/simular", response_model=Response)
async def start_game() -> Response:
    usecase = StartGameUsecase()
    output = await usecase.execute()
    return Response(vencedor=output.vencedor, jogadores=output.jogadores)