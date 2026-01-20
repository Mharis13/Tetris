from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.engine import TetrisEngine
import asyncio

app = FastAPI()

# Configuración de CORS: Vital para que React (puerto 3000) pueda leer de FastAPI (8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O ["*"] para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instanciamos el motor del juego
game = TetrisEngine()


# --- LÓGICA DE ACTUALIZACIÓN AUTOMÁTICA ---
# Esto hace que la pieza caiga sola cada segundo sin necesidad de que el usuario haga nada
async def game_loop():
    while True:
        game.update()
        await asyncio.sleep(1.0)  # La pieza cae cada 1 segundo


@app.on_event("startup")
async def startup_event():
    # Iniciamos el bucle de caída en segundo plano al arrancar el servidor
    asyncio.create_task(game_loop())


# --- RUTAS DE LA API ---


@app.get("/state")
async def get_state():
    """Devuelve la matriz completa para que React la dibuje."""
    return {
        "matrix": game.get_display_grid(),
        "score": game.score,
        "game_over": game.game_over,
    }


@app.post("/move/{direction}")
async def move_piece(direction: str):
    """
    Ruta temporal para mover la pieza con el teclado desde el frontend.
    Direcciones: 'left', 'right', 'down', 'rotate'
    """
    if direction == "left":
        game.move(0, -1)
    elif direction == "right":
        game.move(0, 1)
    elif direction == "down":
        game.move(1, 0)
    elif direction == "rotate":
        game.rotate()  # Lo ismplementaremos en Piece.py

    return {"status": "ok"}
