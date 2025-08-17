````markdown
## 🎲 Game Simulation API

Este projeto é uma API construída com **FastAPI** para simular partidas de um jogo baseado em diferentes estratégias de jogadores.  

---

## 🚀 Tecnologias utilizadas
- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Poetry](https://python-poetry.org/)
- [Uvicorn](https://www.uvicorn.org/)

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/demo-monopoly.git
cd demo-monopoly
````

### 2. Criar o ambiente com Poetry

```bash
poetry shell
poetry install
```

### 3. Executar a API

```bash
uvicorn src.infra.api.main:app --reload
```

### 4. Acessar a documentação interativa

Abra o navegador em:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 Endpoints principais

### `POST /start-game`

Inicia uma nova simulação de jogo.

* **Response**:

```json
{
  "vencedor": "cauteloso",
  "jogadores": ["cauteloso", "impulsivo", "exigente", "aleatorio"]
}
```

---

## 🗂 Estrutura de pastas

```
src/
 ├── application/
 │    └── start_game_usecase.py   # Caso de uso principal
 ├── domain/
 │    ├── game.py                 # Lógica do jogo
 │    ├── jogador.py              # Entidade Jogador
 │    ├── propriedade.py          # Entidade Proriedade
 │    └── strategies.py           # Estratégias
 └── infra/
      └── api/
           └── main.py            # Ponto de entrada FastAPI
```

---

## 📖 Documentação

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## ✅ Requisitos

* Python 3.10 ou superior
* Poetry instalado
