import { useEffect, useState } from 'react'
import './App.css'

// Colores para el tablero
const COLORS: { [key: number]: string } = {
  0: '#1a1a1a', // Fondo
  3: '#FF0000', // Rojo
  4: '#00FF00', // Verde
  5: '#0000FF', // Azul
  6: '#FFFF00', // Amarillo
  7: '#FF00FF', // Magenta
  8: '#00FFFF', // Cian
  9: '#FFA500', // Naranja
};function App() {
  const [grid, setGrid] = useState<number[][]>([]);
  const [score, setScore] = useState(0);
  const [gameOver, setGameOver] = useState(false);

  // 1. POLLING: Pedir el estado al Backend cada 100ms
  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/state');
        if (response.ok) {
          const data = await response.json();
          setGrid(data.matrix);
          setScore(data.score);
          setGameOver(data.game_over);
        }
      } catch (error) {
        console.error("Error conectando con FastAPI. ¿Está el backend encendido?");
      }
    }, 100);
    return () => clearInterval(interval);
  }, []);

  // 2. TECLADO: Enviar movimientos al Backend
  useEffect(() => {
    const handleKeyDown = async (e: KeyboardEvent) => {
      const keysToBlock = ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", " "];

    if (keysToBlock.includes(e.key)) {
      e.preventDefault(); // <-- ESTA ES LA LÍNEA MÁGICA
    }

      let direction = "";
      if (e.key === "ArrowLeft") direction = "left";
      if (e.key === "ArrowRight") direction = "right";
      if (e.key === "ArrowDown") direction = "down";
      if (e.key === "ArrowUp") direction = 'rotate'

      if (direction && !gameOver) {
        await fetch(`http://127.0.0.1:8000/move/${direction}`, { method: 'POST' });
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [gameOver]);

  if (grid.length === 0) {
    return <div className="loading">Cargando tablero desde Python...</div>;
  }

  return (
    <div className="game-container">
      <h1>Tetris Game</h1>
      <div className="status-bar">
        <h2>Score: {score}</h2>
        {gameOver && <h2 className="game-over">¡GAME OVER!</h2>}
      </div>

      <div className="board" style={{
        display: 'grid',
        gridTemplateColumns: `repeat(${grid[0].length}, 30px)`,
        gap: '1px',
        backgroundColor: '#333',
        border: '4px solid #555'
      }}>
        {grid.flat().map((cell, index) => (
          <div
            key={index}
            style={{
              width: '30px',
              height: '30px',
              backgroundColor: COLORS[cell] || '#000'
            }}
          />
        ))}
      </div>
      
      <div className="controls-hint">
        <p>Usa las flechas ← ↓ → para moverte</p>
      </div>
    </div>
  )
}

export default App
