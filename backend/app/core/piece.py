# tetris pieza


import random


class Piece:
    def __init__(self, grid, position=(0, 0), name=""):
        """Inicializa una pieza con una matriz y una posición inicial."""
        self.grid = grid  # Matriz 2D que representa la forma de la pieza
        self.position = position  # Posición (fila, columna) en el tablero
        self.name = name
        self.color_id = random.randint(3, 9)


# Ejemplo de una pieza en forma de L
l_shape = [[1, 0], [1, 0], [1, 1]]

pieza_l = Piece(l_shape)
