class Board:
    """Represents the Tetris board."""

    def __init__(self, rows=20, cols=10):
        """Initialize the board with the specified number of rows and columns."""
        self.rows = rows
        self.cols = cols
        # Renombramos self.board a self.grid para consistencia con el Engine
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def lock_piece(self, piece):
        """
        Fija la pieza en el tablero convirtiendo sus bloques en '1' permanentes.
        Se llama cuando la pieza ya no puede bajar más.
        """
        for row_index, row in enumerate(piece.grid):
            for col_index, cell in enumerate(row):
                if cell:  # Si hay un bloque en la matriz de la pieza
                    board_row = piece.position[0] + row_index
                    board_col = piece.position[1] + col_index

                    # Verificamos que esté dentro de los límites antes de fijar
                    if 0 <= board_row < self.rows and 0 <= board_col < self.cols:
                        self.grid[board_row][board_col] = 1

        # Inmediatamente después de fijar, revisamos si se completaron líneas
        return self.remove_completed_lines()

    def remove_completed_lines(self):
        """
        Busca filas llenas (sin ceros), las elimina y añade filas vacías arriba.
        Devuelve el número de líneas eliminadas (para el score).
        """
        lines_removed = 0
        new_grid = []

        for row in self.grid:
            # Si el 0 no está en la fila, significa que la fila está llena
            if 0 not in row:
                lines_removed += 1
            else:
                # Si no está llena, la mantenemos
                new_grid.append(row)

        # Añadimos tantas filas vacías al principio como líneas hayamos quitado
        for _ in range(lines_removed):
            new_grid.insert(0, [0 for _ in range(self.cols)])

        self.grid = new_grid
        return lines_removed

    def is_collision(self, piece):
        """Verifica si hay una colisión con la pieza en el tablero."""
        for row_index, row in enumerate(piece.grid):
            for col_index, cell in enumerate(row):
                if cell:
                    board_row = piece.position[0] + row_index
                    board_col = piece.position[1] + col_index

                    # 1. Colisión con el suelo
                    if board_row >= self.rows:
                        return True
                    # 2. Colisión con paredes laterales
                    if board_col < 0 or board_col >= self.cols:
                        return True
                    # 3. Colisión con piezas ya fijas (solo si board_row es positivo)
                    if board_row >= 0 and self.grid[board_row][board_col] != 0:
                        return True
        return False
