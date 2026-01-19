from .board import Board
from .piece import Piece
import random


class TetrisEngine:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.board = Board(self.rows, self.cols)
        self.current_piece = self._spawn_piece()
        self.game_over = False
        self.score = 0

    def _spawn_piece(self):
        """Crea una nueva pieza aleatoria en la parte superior central."""
        # Aquí defines tus formas. Ejemplo simple: una L
        shapes = [
            [[1, 1], [1, 1]],  # Cuadrado
        ]
        shape = random.choice(shapes)
        # La pieza empieza en la fila 0, columna central (4)
        return Piece(grid=shape, position=[0, 4])

    def update(self):
        """Lógica de caída automática (Gravedad)."""
        if self.game_over:
            return

        # Intentamos mover hacia abajo (1 fila hacia abajo, 0 columnas lateral)
        if not self.move(1, 0):
            # Si NO pudo moverse hacia abajo, hay colisión (suelo o pieza)
            self.board.lock_piece(self.current_piece)

            # Limpiar líneas y sumar puntos (opcional por ahora)
            # self.score += self.board.clear_lines()

            # Generar nueva pieza
            self.current_piece = self._spawn_piece()

            # Si la nueva pieza aparece y ya choca, es Game Over
            if self.board.is_collision(self.current_piece):
                self.game_over = True
                print("GAME OVER")

    def move(self, dr, dc):
        """Intenta mover la pieza. Devuelve True si fue posible."""
        # 1. Mover tentativamente
        self.current_piece.position[0] += dr
        self.current_piece.position[1] += dc

        # 2. Verificar si el nuevo lugar es legal
        if self.board.is_collision(self.current_piece):
            # 3. Si es ilegal, deshacer el movimiento
            self.current_piece.position[0] -= dr
            self.current_piece.position[1] -= dc
            return False

        return True

    def get_display_grid(self):
        """
        Une el tablero fijo con la pieza que está cayendo
        para enviarlo al frontend.
        """
        # Copiamos la matriz del tablero para no modificar la original
        grid_copy = [row[:] for row in self.board.grid]

        # "Pintamos" la pieza actual en la copia con el valor 2 (Rojo en React)
        for r_idx, row in enumerate(self.current_piece.grid):
            for c_idx, cell in enumerate(row):
                if cell:
                    board_r = self.current_piece.position[0] + r_idx
                    board_c = self.current_piece.position[1] + c_idx

                    # Verificamos que esté dentro de los límites antes de pintar
                    # (esto evita errores visuales al spawnear)
                    if 0 <= board_r < self.rows and 0 <= board_c < self.cols:
                        grid_copy[board_r][board_c] = 2

        return grid_copy
