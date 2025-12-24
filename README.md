# 🎮 Tetris Autoritario

Sistema Tetris donde el servidor tiene control total del juego, implementando validación anti-cheat, autenticación JWT, y leaderboard global con Redis.

## 📋 Gestión del Proyecto

Este repositorio incluye una planificación completa estilo Trello para el desarrollo del proyecto:

### Documentos de Planificación

- **[PROJECT_PLAN.md](PROJECT_PLAN.md)** - Plan detallado con 40 tareas técnicas atómicas organizadas en 8 hitos
- **[TRELLO_BOARD.md](TRELLO_BOARD.md)** - Visualización estilo Trello con columnas TO DO, DOING, DONE
- **[issues/TETRIS_ISSUES.json](issues/TETRIS_ISSUES.json)** - Formato JSON para importación a herramientas de gestión (Trello, Jira, GitHub Projects)

### Estructura del Proyecto (Planificado)

```
Tetris/
├── backend/              # Node.js + Socket.io + TypeScript
│   ├── src/
│   │   ├── server/      # Servidor HTTP y Socket.io
│   │   ├── game/        # Lógica del juego (matriz, tetrominos, validación)
│   │   ├── auth/        # JWT (Aegis) y autenticación
│   │   └── redis/       # Cliente Redis y leaderboard
│   └── package.json
├── frontend/            # React + TypeScript + Vite
│   ├── src/
│   │   ├── components/  # Componentes UI (GameBoard, ScorePanel, etc.)
│   │   ├── hooks/       # Custom hooks (useGameState, useKeyboard)
│   │   ├── services/    # SocketService, AuthService
│   │   └── types/       # Tipos TypeScript compartidos
│   └── package.json
├── shared/              # Tipos e interfaces compartidas
└── package.json         # Monorepo workspace
```

## 🏗️ Stack Tecnológico

### Backend
- **Runtime**: Node.js v18+
- **Framework**: Socket.io v4+ para comunicación real-time
- **Autenticación**: JWT con Aegis
- **Base de Datos**: Redis (Sorted Sets para leaderboard)
- **Lenguaje**: TypeScript (strict mode)

### Frontend
- **Framework**: React 18+ con TypeScript
- **Build Tool**: Vite
- **Estado**: Context API + Custom Hooks
- **Comunicación**: Socket.io Client

### DevOps
- **Containerización**: Docker + docker-compose
- **CI/CD**: GitHub Actions
- **Testing**: Jest (backend), React Testing Library (frontend), Playwright (E2E)
- **Monitoreo**: Winston para logging

## 🎯 Características Principales

### ✅ Control Total del Servidor (Autoritario)
- Toda la lógica del juego ejecuta en el servidor
- El cliente solo renderiza el estado recibido
- Sistema anti-cheat con validación server-side de cada movimiento

### ✅ Validación Anti-Cheat
- Validación de colisiones con bordes y piezas existentes
- Validación de rotaciones con wall-kick
- Rate limiting de acciones (20/segundo)
- Logging de intentos de trampa

### ✅ Autenticación Segura
- JWT (Aegis) con tokens de acceso (24h) y refresh (7d)
- Middleware de autenticación en Socket.io
- Hashing de passwords con bcrypt (12 rounds)

### ✅ Leaderboard Global
- Redis Sorted Sets para ranking eficiente
- Leaderboards: Global, Daily, Weekly
- API REST para consultas
- Actualización en tiempo real

### ✅ Sistema de Juego Completo
- Matriz 10x20 estándar
- 7 tipos de tetrominos (I, O, T, S, Z, J, L)
- Sistema de rotación SRS (Super Rotation System)
- Tick rate de caída configurable y progresivo
- Sistema de puntuación con niveles
- Hold piece y preview de siguientes piezas

### ✅ Reconexión Automática
- Recuperación de estado tras desconexión (5 min)
- Auto-reconexión del cliente Socket.io
- Reanudación de partida desde último estado

## 📊 Hitos del Proyecto

| Hito | Descripción | Tareas | Estimación |
|------|-------------|---------|------------|
| **H1** | Configuración Inicial | 3 | 8h |
| **H2** | Backend - Core Tetris | 7 | 31h |
| **H3** | Socket.io Server | 5 | 24h |
| **H4** | Autenticación JWT | 4 | 18h |
| **H5** | Redis Leaderboard | 4 | 18h |
| **H6** | Frontend React | 9 | 41h |
| **H7** | Testing y Calidad | 4 | 28h |
| **H8** | DevOps y Deployment | 4 | 18h |
| **TOTAL** | | **40 tareas** | **186h** |

## 🚀 Roadmap

### Sprint 1 (Semana 1): Fundamentos
- Setup de monorepo
- Lógica core del juego
- Autenticación básica

### Sprint 2 (Semana 2): Backend Completo
- Game logic completa
- Socket.io con rooms
- Redis con leaderboard

### Sprint 3 (Semana 3): Frontend Completo
- Auth middleware crítico
- UI del juego funcional
- Sistema de input

### Sprint 4 (Semana 4): Integración y Pulido
- UI completa
- Sistema de reconexión
- Tests backend y frontend

### Sprint 5 (Semana 5): DevOps y Extras
- Leaderboards temporales
- Docker y CI/CD
- Tests E2E y documentación

## 📦 Instalación (Futuro)

```bash
# Clonar repositorio
git clone https://github.com/Mharis13/Tetris.git
cd Tetris

# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env

# Levantar servicios con Docker
docker-compose up -d

# Acceder a la aplicación
# Frontend: http://localhost:5173
# Backend: http://localhost:3000
# API Docs: http://localhost:3000/api-docs
```

## 🧪 Testing (Futuro)

```bash
# Tests unitarios backend
npm run test:backend

# Tests unitarios frontend
npm run test:frontend

# Tests E2E
npm run test:e2e

# Cobertura de código
npm run test:coverage
```

## 📚 Documentación

- **Arquitectura**: Ver [PROJECT_PLAN.md](PROJECT_PLAN.md) sección "Decisiones de Arquitectura"
- **API REST**: Swagger UI disponible en `/api-docs` (post-implementación)
- **Eventos Socket.io**: Documentados en [PROJECT_PLAN.md](PROJECT_PLAN.md)
- **Issues y Tareas**: Ver [TRELLO_BOARD.md](TRELLO_BOARD.md) o [issues/](issues/)

## 🤝 Contribución

Este es un proyecto educativo. Para contribuir:

1. Revisar [TRELLO_BOARD.md](TRELLO_BOARD.md) para ver tareas disponibles
2. Asignarse una tarea en estado TO DO
3. Crear branch: `git checkout -b feature/TASK-XXX`
4. Implementar siguiendo los criterios de aceptación
5. Crear Pull Request con tests pasando

## 📝 Licencia

Ver archivo [LICENSE](LICENSE) para más detalles.

## 🎯 Métricas de Éxito

### Técnicas
- ✅ Cobertura de tests >80% backend, >70% frontend
- ✅ Latencia Socket.io <50ms promedio
- ✅ Tick rate estable 60 FPS
- ✅ 100% validación server-side

### Producto
- ✅ Tiempo de partida: 3-10 min promedio
- ✅ Soportar 100+ usuarios concurrentes
- ✅ Leaderboard actualizado <1s
- ✅ Reconexión <3s

---

**Estado del Proyecto**: 📋 Planificación Completa  
**Versión**: 1.0.0  
**Última Actualización**: 2025-12-24