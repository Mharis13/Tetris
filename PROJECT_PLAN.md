# Tetris Autoritario - Project Plan

## Visión General del Proyecto
Sistema Tetris autoritario donde el servidor controla completamente el estado del juego, validando cada movimiento (anti-cheat), gestionando el tick rate de caída, y el cliente solo renderiza el estado recibido.

## Arquitectura Técnica
- **Backend**: Node.js + Socket.io
- **Autenticación**: JWT (Aegis)
- **Base de Datos**: Redis (Sorted Sets para Leaderboard)
- **Frontend**: React + TypeScript

---

## 📋 BACKLOG - ESTILO TRELLO

### 🔵 TO DO

#### HITO 1: Configuración Inicial del Proyecto (Sprint 0)

**TASK-001: Inicializar Monorepo**
- **Descripción**: Configurar estructura de monorepo con workspace para backend y frontend
- **Criterios de Aceptación**:
  - [ ] Estructura de directorios: `/backend`, `/frontend`, `/shared`
  - [ ] package.json raíz con workspaces configurados
  - [ ] .gitignore configurado para node_modules, .env, dist
  - [ ] README.md actualizado con instrucciones de setup
- **Estimación**: 2h
- **Dependencias**: Ninguna
- **Etiquetas**: `setup`, `infrastructure`

**TASK-002: Configurar Backend Base**
- **Descripción**: Inicializar proyecto Node.js con TypeScript y estructura base
- **Criterios de Aceptación**:
  - [ ] Node.js v18+ configurado
  - [ ] TypeScript configurado con strict mode
  - [ ] ESLint + Prettier configurados
  - [ ] Scripts npm: dev, build, start
  - [ ] Estructura de carpetas: src/{server, game, auth, redis}
- **Estimación**: 3h
- **Dependencias**: TASK-001
- **Etiquetas**: `backend`, `setup`

**TASK-003: Configurar Frontend Base**
- **Descripción**: Inicializar proyecto React + TypeScript con Vite
- **Criterios de Aceptación**:
  - [ ] Vite + React + TypeScript configurado
  - [ ] ESLint + Prettier configurados
  - [ ] Estructura de carpetas: src/{components, hooks, services, types}
  - [ ] Scripts npm: dev, build, preview
  - [ ] Hot reload funcionando
- **Estimación**: 3h
- **Dependencias**: TASK-001
- **Etiquetas**: `frontend`, `setup`

---

#### HITO 2: Backend - Sistema Core de Tetris

**TASK-004: Implementar Matriz de Juego (10x20)**
- **Descripción**: Crear clase GameBoard que gestione la matriz 10x20 del tablero
- **Criterios de Aceptación**:
  - [ ] Clase GameBoard con matriz 10x20 inicializada
  - [ ] Métodos: getCell(x, y), setCell(x, y, value), clearRow(y)
  - [ ] Validación de límites de coordenadas
  - [ ] Tests unitarios con cobertura >80%
  - [ ] Tipos TypeScript para Cell, Board, Coordinates
- **Estimación**: 4h
- **Dependencias**: TASK-002
- **Etiquetas**: `backend`, `game-logic`, `core`

**TASK-005: Implementar Sistema de Tetrominos**
- **Descripción**: Crear clases para los 7 tipos de tetrominos (I, O, T, S, Z, J, L)
- **Criterios de Aceptación**:
  - [ ] Enum TetrominoType con 7 tipos
  - [ ] Clase Tetromino con propiedades: type, position, rotation
  - [ ] Matrices de rotación para cada tipo (0°, 90°, 180°, 270°)
  - [ ] Método rotate() con sistema SRS (Super Rotation System)
  - [ ] Tests para cada tipo de pieza y rotaciones
- **Estimación**: 6h
- **Dependencias**: TASK-004
- **Etiquetas**: `backend`, `game-logic`, `core`

**TASK-006: Implementar Validación de Movimientos (Anti-Cheat)**
- **Descripción**: Sistema de validación server-side para todos los movimientos
- **Criterios de Aceptación**:
  - [ ] Método validateMove(tetromino, board): boolean
  - [ ] Validar colisiones con bordes
  - [ ] Validar colisiones con piezas existentes
  - [ ] Validar rotaciones con wall-kick
  - [ ] Log de intentos de trampas
  - [ ] Tests de edge cases (movimientos inválidos)
- **Estimación**: 5h
- **Dependencias**: TASK-005
- **Etiquetas**: `backend`, `game-logic`, `security`, `critical`

**TASK-007: Implementar Tick Rate de Caída**
- **Descripción**: Sistema de gravedad automática basado en intervalos
- **Criterios de Aceptación**:
  - [ ] Clase GameTicker con setInterval configurable
  - [ ] Tick rate inicial: 1000ms (1 segundo)
  - [ ] Aceleración progresiva: -50ms cada 10 líneas
  - [ ] Tick rate mínimo: 100ms
  - [ ] Pausar/reanudar funcionalidad
  - [ ] Evento onTick que mueve pieza hacia abajo
- **Estimación**: 4h
- **Dependencias**: TASK-006
- **Etiquetas**: `backend`, `game-logic`, `core`

**TASK-008: Implementar Detección de Líneas Completas**
- **Descripción**: Sistema para detectar y eliminar líneas completas
- **Criterios de Aceptación**:
  - [ ] Método detectFullRows(): number[]
  - [ ] Método clearRows(rows: number[]): void
  - [ ] Aplicar gravedad a filas superiores
  - [ ] Calcular puntuación: 100 (1 línea), 300 (2), 500 (3), 800 (4)
  - [ ] Evento onLinesCleared con puntuación
  - [ ] Tests para casos múltiples líneas
- **Estimación**: 4h
- **Dependencias**: TASK-004
- **Etiquetas**: `backend`, `game-logic`, `core`

**TASK-009: Implementar Sistema de Puntuación**
- **Descripción**: Sistema de scoring con nivel y multiplicadores
- **Criterios de Aceptación**:
  - [ ] Clase ScoreManager con score, level, lines
  - [ ] Cálculo de nivel: floor(lines / 10)
  - [ ] Puntos por pieza colocada: 10 * level
  - [ ] Puntos por soft drop: 1 por celda
  - [ ] Puntos por hard drop: 2 por celda
  - [ ] Persistencia de high score
- **Estimación**: 3h
- **Dependencias**: TASK-008
- **Etiquetas**: `backend`, `game-logic`, `scoring`

**TASK-010: Implementar Game State Manager**
- **Descripción**: Clase que gestiona el estado completo del juego por usuario
- **Criterios de Aceptación**:
  - [ ] Clase GameState con: board, currentPiece, nextPieces, score, level
  - [ ] Estados: IDLE, PLAYING, PAUSED, GAME_OVER
  - [ ] Métodos: startGame(), pauseGame(), endGame()
  - [ ] Serialización del estado completo a JSON
  - [ ] Validación de transiciones de estado
  - [ ] Tests de integración del flujo completo
- **Estimación**: 5h
- **Dependencias**: TASK-009
- **Etiquetas**: `backend`, `game-logic`, `core`, `critical`

---

#### HITO 3: Backend - Socket.io Server

**TASK-011: Configurar Socket.io Server**
- **Descripción**: Configurar servidor Socket.io con CORS y middleware
- **Criterios de Aceptación**:
  - [ ] Socket.io v4+ instalado y configurado
  - [ ] CORS configurado para frontend origin
  - [ ] Middleware de autenticación
  - [ ] Namespace `/game` creado
  - [ ] Event logging middleware
  - [ ] Manejo de errores global
- **Estimación**: 4h
- **Dependencias**: TASK-002
- **Etiquetas**: `backend`, `socket.io`, `infrastructure`

**TASK-012: Implementar Room Manager**
- **Descripción**: Sistema de salas para partidas individuales por usuario
- **Criterios de Aceptación**:
  - [ ] Map<userId, GameState> para gestionar partidas activas
  - [ ] Método createRoom(userId): roomId
  - [ ] Método joinRoom(userId, roomId): boolean
  - [ ] Método leaveRoom(userId): void
  - [ ] Cleanup automático de salas inactivas (30 min)
  - [ ] Límite de 1 partida activa por usuario
- **Estimación**: 5h
- **Dependencias**: TASK-011
- **Etiquetas**: `backend`, `socket.io`, `rooms`

**TASK-013: Implementar Event Handlers - Input del Cliente**
- **Descripción**: Handlers para eventos del cliente: move, rotate, drop
- **Criterios de Aceptación**:
  - [ ] Handler `player:move` (left, right, down)
  - [ ] Handler `player:rotate` (clockwise, counterclockwise)
  - [ ] Handler `player:hard-drop`
  - [ ] Handler `player:hold-piece`
  - [ ] Validación anti-cheat en cada handler
  - [ ] Rate limiting: máx 20 acciones/segundo
  - [ ] Emisión de estado actualizado tras cada acción
- **Estimación**: 6h
- **Dependencias**: TASK-012, TASK-006
- **Etiquetas**: `backend`, `socket.io`, `event-handlers`, `critical`

**TASK-014: Implementar Event Emitters - Estado del Servidor**
- **Descripción**: Emisión de eventos del servidor al cliente
- **Criterios de Aceptación**:
  - [ ] Evento `game:state-update` con estado completo
  - [ ] Evento `game:tick` para caída automática
  - [ ] Evento `game:lines-cleared` con puntuación
  - [ ] Evento `game:game-over` con puntuación final
  - [ ] Evento `game:error` con mensaje de error
  - [ ] Throttling de actualizaciones: 60 FPS máx
- **Estimación**: 4h
- **Dependencias**: TASK-013
- **Etiquetas**: `backend`, `socket.io`, `event-emitters`

**TASK-015: Implementar Sistema de Reconexión**
- **Descripción**: Recuperación de estado tras desconexión del cliente
- **Criterios de Aceptación**:
  - [ ] Persistir estado en memoria durante 5 minutos post-desconexión
  - [ ] Handler `player:reconnect` con recuperación de estado
  - [ ] Validación de identidad del usuario (JWT)
  - [ ] Reanudar ticker desde último estado
  - [ ] Notificación al cliente de estado recuperado
- **Estimación**: 5h
- **Dependencias**: TASK-014
- **Etiquetas**: `backend`, `socket.io`, `reliability`

---

#### HITO 4: Autenticación con JWT (Aegis)

**TASK-016: Configurar Aegis JWT**
- **Descripción**: Instalar y configurar biblioteca Aegis para JWT
- **Criterios de Aceptación**:
  - [ ] Aegis (o jsonwebtoken) instalado
  - [ ] Secret key cargada desde .env
  - [ ] Token lifetime: 24h
  - [ ] Refresh token lifetime: 7d
  - [ ] Algoritmo HS256 configurado
  - [ ] Tipos TypeScript para JWTPayload
- **Estimación**: 3h
- **Dependencias**: TASK-002
- **Etiquetas**: `backend`, `auth`, `security`

**TASK-017: Implementar Endpoints de Autenticación**
- **Descripción**: REST endpoints para registro, login, refresh
- **Criterios de Aceptación**:
  - [ ] POST /auth/register (username, password)
  - [ ] POST /auth/login (username, password)
  - [ ] POST /auth/refresh (refreshToken)
  - [ ] POST /auth/logout
  - [ ] Validación de entrada con Zod
  - [ ] Hashing de passwords con bcrypt (12 rounds)
  - [ ] Respuesta con accessToken y refreshToken
- **Estimación**: 6h
- **Dependencias**: TASK-016
- **Etiquetas**: `backend`, `auth`, `endpoints`, `critical`

**TASK-018: Implementar Middleware de Autenticación Socket.io**
- **Descripción**: Middleware para validar JWT en conexión Socket.io
- **Criterios de Aceptación**:
  - [ ] Middleware que intercepta handshake
  - [ ] Extrae token de auth.token o query.token
  - [ ] Valida token con Aegis
  - [ ] Adjunta userId al socket
  - [ ] Rechaza conexión si token inválido
  - [ ] Tests con tokens válidos/inválidos/expirados
- **Estimación**: 4h
- **Dependencias**: TASK-017, TASK-011
- **Etiquetas**: `backend`, `auth`, `socket.io`, `security`, `critical`

**TASK-019: Implementar Sistema de Usuarios**
- **Descripción**: Modelo de usuarios con persistencia en Redis
- **Criterios de Aceptación**:
  - [ ] Interfaz User: userId, username, passwordHash, createdAt
  - [ ] Métodos: createUser, findUserByUsername, findUserById
  - [ ] Almacenamiento en Redis con prefijo `user:`
  - [ ] Username único (validación)
  - [ ] Email opcional para recuperación
- **Estimación**: 5h
- **Dependencias**: TASK-016
- **Etiquetas**: `backend`, `auth`, `database`

---

#### HITO 5: Redis - Leaderboard Global

**TASK-020: Configurar Conexión a Redis**
- **Descripción**: Setup de cliente Redis con retry logic
- **Criterios de Aceptación**:
  - [ ] ioredis instalado y configurado
  - [ ] Conexión a Redis (localhost:6379 o env variable)
  - [ ] Retry strategy: 3 intentos con backoff
  - [ ] Health check endpoint /health/redis
  - [ ] Graceful shutdown on SIGTERM
  - [ ] Tests de conexión y desconexión
- **Estimación**: 4h
- **Dependencias**: TASK-002
- **Etiquetas**: `backend`, `redis`, `infrastructure`

**TASK-021: Implementar Leaderboard con Sorted Sets**
- **Descripción**: Sistema de ranking global usando ZADD/ZRANGE
- **Criterios de Aceptación**:
  - [ ] Sorted Set `leaderboard:global` con scores
  - [ ] Método addScore(userId, score): void
  - [ ] Método getTopPlayers(limit): Player[]
  - [ ] Método getUserRank(userId): number
  - [ ] Método getUserScore(userId): number
  - [ ] Actualización atómica con ZINCRBY
  - [ ] Tests con múltiples usuarios y scores
- **Estimación**: 5h
- **Dependencias**: TASK-020
- **Etiquetas**: `backend`, `redis`, `leaderboard`, `core`

**TASK-022: Implementar API REST para Leaderboard**
- **Descripción**: Endpoints públicos para consultar leaderboard
- **Criterios de Aceptación**:
  - [ ] GET /leaderboard/top/:limit
  - [ ] GET /leaderboard/user/:userId
  - [ ] GET /leaderboard/rank/:userId
  - [ ] Cache de respuestas (60 segundos)
  - [ ] Paginación para top N
  - [ ] Formato JSON estándar
- **Estimación**: 3h
- **Dependencias**: TASK-021
- **Etiquetas**: `backend`, `redis`, `api`, `leaderboard`

**TASK-023: Implementar Sistema de Daily/Weekly Leaderboards**
- **Descripción**: Leaderboards temporales con TTL automático
- **Criterios de Aceptación**:
  - [ ] Sorted Set `leaderboard:daily:{date}`
  - [ ] Sorted Set `leaderboard:weekly:{week}`
  - [ ] TTL automático: 24h (daily), 7d (weekly)
  - [ ] Actualización paralela con global
  - [ ] Endpoints GET para cada leaderboard
  - [ ] Cron job para reset diario/semanal
- **Estimación**: 6h
- **Dependencias**: TASK-021
- **Etiquetas**: `backend`, `redis`, `leaderboard`, `scheduling`

---

#### HITO 6: Frontend React + TypeScript

**TASK-024: Configurar Cliente Socket.io**
- **Descripción**: Setup de socket.io-client con auto-reconexión
- **Criterios de Aceptación**:
  - [ ] socket.io-client instalado
  - [ ] Servicio SocketService como singleton
  - [ ] Auto-reconexión habilitada
  - [ ] Event listeners tipo-safe con TypeScript
  - [ ] Manejo de estados: connecting, connected, disconnected
  - [ ] Hook useSocket() para componentes
- **Estimación**: 4h
- **Dependencias**: TASK-003
- **Etiquetas**: `frontend`, `socket.io`, `infrastructure`

**TASK-025: Implementar Sistema de Autenticación Frontend**
- **Descripción**: Login/Register forms con gestión de tokens
- **Criterios de Aceptación**:
  - [ ] Componente LoginForm con validación
  - [ ] Componente RegisterForm con validación
  - [ ] AuthContext para estado global de auth
  - [ ] LocalStorage para persistir tokens
  - [ ] Auto-refresh de tokens antes de expirar
  - [ ] Redirección a /login si no autenticado
- **Estimación**: 6h
- **Dependencias**: TASK-024, TASK-017
- **Etiquetas**: `frontend`, `auth`, `ui`

**TASK-026: Implementar Hook useGameState**
- **Descripción**: Custom hook para suscribirse al estado del juego
- **Criterios de Aceptación**:
  - [ ] Hook useGameState() que escucha `game:state-update`
  - [ ] Estado local sincronizado con servidor
  - [ ] Tipos TypeScript para GameState
  - [ ] Manejo de loading y error states
  - [ ] Re-render optimizado con useMemo
  - [ ] Tests con React Testing Library
- **Estimación**: 4h
- **Dependencias**: TASK-024
- **Etiquetas**: `frontend`, `hooks`, `state-management`

**TASK-027: Implementar Componente GameBoard**
- **Descripción**: Renderizado de matriz 10x20 con canvas o divs
- **Criterios de Aceptación**:
  - [ ] Componente GameBoard que recibe matriz 10x20
  - [ ] Renderizado con CSS Grid o Canvas
  - [ ] Colores distintos por tipo de tetromino
  - [ ] Celdas de 30x30px
  - [ ] Animación suave de piezas cayendo
  - [ ] Responsive (escala en móviles)
- **Estimación**: 6h
- **Dependencias**: TASK-026
- **Etiquetas**: `frontend`, `ui`, `game-view`, `critical`

**TASK-028: Implementar Componente NextPieces**
- **Descripción**: Vista previa de siguiente(s) pieza(s)
- **Criterios de Aceptación**:
  - [ ] Componente NextPieces que muestra 3 siguientes piezas
  - [ ] Mini-grid 4x4 por pieza
  - [ ] Colores consistentes con GameBoard
  - [ ] Posicionado a la derecha del tablero
  - [ ] Diseño tipo Tetris oficial
- **Estimación**: 3h
- **Dependencias**: TASK-027
- **Etiquetas**: `frontend`, `ui`, `game-view`

**TASK-029: Implementar Sistema de Input del Jugador**
- **Descripción**: Captura de teclas y emisión de eventos al servidor
- **Criterios de Aceptación**:
  - [ ] Hook useKeyboard() para detectar teclas
  - [ ] Mapeo: ArrowLeft (mover izq), ArrowRight (mover der)
  - [ ] Mapeo: ArrowDown (soft drop), Space (hard drop)
  - [ ] Mapeo: ArrowUp o Z/X (rotar)
  - [ ] Mapeo: C o Shift (hold piece)
  - [ ] Emitir eventos al servidor vía socket
  - [ ] Debounce para prevenir spam
- **Estimación**: 5h
- **Dependencias**: TASK-024
- **Etiquetas**: `frontend`, `input`, `user-interaction`, `critical`

**TASK-030: Implementar Componente ScorePanel**
- **Descripción**: Panel con score, nivel, líneas, leaderboard
- **Criterios de Aceptación**:
  - [ ] Mostrar: Score actual, Nivel, Líneas completadas
  - [ ] Mostrar: High Score personal
  - [ ] Mostrar: Top 5 del leaderboard global
  - [ ] Actualización en tiempo real
  - [ ] Diseño lateral o superior
- **Estimación**: 4h
- **Dependencias**: TASK-026, TASK-022
- **Etiquetas**: `frontend`, `ui`, `score`

**TASK-031: Implementar Pantallas de Estado (Game Over, Pause)**
- **Descripción**: Overlays para estados no-jugables
- **Criterios de Aceptación**:
  - [ ] Modal GameOver con score final y botón "Jugar de Nuevo"
  - [ ] Modal Pause con botón "Reanudar"
  - [ ] Modal Connecting si conexión se pierde
  - [ ] Diseño con transparencia sobre el tablero
  - [ ] Animaciones de entrada/salida
- **Estimación**: 4h
- **Dependencias**: TASK-027
- **Etiquetas**: `frontend`, `ui`, `game-states`

**TASK-032: Implementar Leaderboard View**
- **Descripción**: Página completa de leaderboard con tabs
- **Criterios de Aceptación**:
  - [ ] Tabs: Global, Daily, Weekly
  - [ ] Tabla con columnas: Rank, Usuario, Score, Fecha
  - [ ] Highlight del usuario actual
  - [ ] Paginación (50 por página)
  - [ ] Auto-refresh cada 30 segundos
  - [ ] Skeleton loading state
- **Estimación**: 5h
- **Dependencias**: TASK-022, TASK-023
- **Etiquetas**: `frontend`, `ui`, `leaderboard`

---

#### HITO 7: Testing y Calidad

**TASK-033: Tests Unitarios Backend**
- **Descripción**: Cobertura de tests para lógica core del backend
- **Criterios de Aceptación**:
  - [ ] Jest configurado con TypeScript
  - [ ] Tests para GameBoard, Tetromino, Validation
  - [ ] Tests para ScoreManager
  - [ ] Tests para JWT generation/validation
  - [ ] Cobertura >80% en /src/game
  - [ ] Ejecución con `npm test`
- **Estimación**: 8h
- **Dependencias**: TASK-010
- **Etiquetas**: `backend`, `testing`, `quality`

**TASK-034: Tests de Integración Socket.io**
- **Descripción**: Tests end-to-end del flujo Socket.io
- **Criterios de Aceptación**:
  - [ ] Socket.io-client en tests con mock server
  - [ ] Test: Conectar con JWT válido
  - [ ] Test: Rechazo con JWT inválido
  - [ ] Test: Flujo completo de partida
  - [ ] Test: Reconexión tras desconexión
  - [ ] Ejecución aislada con servidor test
- **Estimación**: 6h
- **Dependencias**: TASK-015, TASK-018
- **Etiquetas**: `backend`, `testing`, `integration`

**TASK-035: Tests Frontend con React Testing Library**
- **Descripción**: Tests de componentes y hooks
- **Criterios de Aceptación**:
  - [ ] React Testing Library configurado
  - [ ] Tests para LoginForm, RegisterForm
  - [ ] Tests para GameBoard rendering
  - [ ] Tests para useGameState hook
  - [ ] Tests para useKeyboard hook
  - [ ] Cobertura >70% en componentes críticos
- **Estimación**: 6h
- **Dependencias**: TASK-031
- **Etiquetas**: `frontend`, `testing`, `quality`

**TASK-036: Tests E2E con Playwright**
- **Descripción**: Tests end-to-end del flujo completo
- **Criterios de Aceptación**:
  - [ ] Playwright configurado
  - [ ] Test: Registro → Login → Jugar partida
  - [ ] Test: Movimientos básicos y rotaciones
  - [ ] Test: Game Over y restart
  - [ ] Test: Leaderboard actualizado tras partida
  - [ ] CI/CD pipeline ejecuta tests E2E
- **Estimación**: 8h
- **Dependencias**: TASK-032
- **Etiquetas**: `e2e`, `testing`, `quality`

---

#### HITO 8: DevOps y Deployment

**TASK-037: Configurar Docker**
- **Descripción**: Dockerfiles y docker-compose para desarrollo
- **Criterios de Aceptación**:
  - [ ] Dockerfile para backend (multi-stage)
  - [ ] Dockerfile para frontend (nginx)
  - [ ] docker-compose.yml con: backend, frontend, redis
  - [ ] Variables de entorno en .env.example
  - [ ] Volúmenes persistentes para Redis
  - [ ] `docker-compose up` levanta todo el stack
- **Estimación**: 5h
- **Dependencias**: TASK-020
- **Etiquetas**: `devops`, `docker`, `infrastructure`

**TASK-038: Configurar CI/CD Pipeline**
- **Descripción**: GitHub Actions para CI/CD
- **Criterios de Aceptación**:
  - [ ] Workflow para pull requests: lint, test, build
  - [ ] Workflow para main: deploy a staging
  - [ ] Cacheo de node_modules
  - [ ] Code coverage reports
  - [ ] Notificaciones de fallos
  - [ ] Secrets para credenciales
- **Estimación**: 5h
- **Dependencias**: TASK-033, TASK-035
- **Etiquetas**: `devops`, `ci-cd`, `automation`

**TASK-039: Configurar Monitoreo y Logging**
- **Descripción**: Winston para logs estructurados y métricas
- **Criterios de Aceptación**:
  - [ ] Winston configurado con niveles: error, warn, info, debug
  - [ ] Logs rotativos (1 archivo por día)
  - [ ] Contexto en logs: userId, roomId, action
  - [ ] Métricas: partidas activas, usuarios conectados
  - [ ] Dashboard básico (opcional: Grafana)
- **Estimación**: 4h
- **Dependencias**: TASK-014
- **Etiquetas**: `devops`, `observability`, `logging`

**TASK-040: Documentación de API**
- **Descripción**: Swagger/OpenAPI para REST endpoints
- **Criterios de Aceptación**:
  - [ ] Swagger UI en /api-docs
  - [ ] Documentación de todos los endpoints REST
  - [ ] Ejemplos de request/response
  - [ ] Documentación de eventos Socket.io
  - [ ] README con arquitectura y setup
- **Estimación**: 4h
- **Dependencias**: TASK-022
- **Etiquetas**: `documentation`, `api`

---

### 🟡 DOING

*(Tareas actualmente en progreso)*

**TASK-041: Crear Documento de Issues Trello**
- **Descripción**: Generar este documento con todas las tareas
- **Criterios de Aceptación**:
  - [x] Estructura TO DO, DOING, DONE
  - [x] Tareas atómicas con estimaciones
  - [x] Hitos definidos
  - [x] Criterios de aceptación específicos
  - [x] Dependencias mapeadas
  - [ ] Revisión y aprobación del PM
- **Estimación**: 4h
- **Etiquetas**: `documentation`, `planning`

---

### 🟢 DONE

*(Tareas completadas)*

---

## 📊 RESUMEN DE HITOS

| Hito | Tareas | Estimación Total | Dependencias Críticas |
|------|---------|------------------|----------------------|
| **H1: Setup Inicial** | 3 | 8h | Ninguna |
| **H2: Backend Core** | 7 | 31h | H1 |
| **H3: Socket.io** | 5 | 24h | H1, H2 |
| **H4: Autenticación** | 4 | 18h | H1, H3 |
| **H5: Redis** | 4 | 18h | H1 |
| **H6: Frontend** | 9 | 41h | H1, H3, H4, H5 |
| **H7: Testing** | 4 | 28h | H2, H3, H6 |
| **H8: DevOps** | 4 | 18h | H5, H7 |
| **TOTAL** | **40 tareas** | **186h** (~4-5 semanas con 1 dev) |

---

## 🎯 PRIORIDADES Y CAMINO CRÍTICO

### Sprint 1 (Semana 1): Fundamentos
- TASK-001 → TASK-002 → TASK-003 (Setup)
- TASK-004 → TASK-005 → TASK-006 (Game Logic Core)
- TASK-016 → TASK-017 (Auth Básico)

### Sprint 2 (Semana 2): Backend Completo
- TASK-007 → TASK-008 → TASK-009 → TASK-010 (Game Logic)
- TASK-011 → TASK-012 → TASK-013 → TASK-014 (Socket.io)
- TASK-020 → TASK-021 (Redis Básico)

### Sprint 3 (Semana 3): Frontend Completo
- TASK-018 (Auth Middleware - CRÍTICO)
- TASK-024 → TASK-025 (Socket Frontend + Auth)
- TASK-026 → TASK-027 → TASK-029 (Game View + Input)
- TASK-022 (Leaderboard API)

### Sprint 4 (Semana 4): Integración y Pulido
- TASK-028 → TASK-030 → TASK-031 (UI Completa)
- TASK-032 (Leaderboard View)
- TASK-015 (Reconexión)
- TASK-033 → TASK-034 → TASK-035 (Tests)

### Sprint 5 (Semana 5): DevOps y Extras
- TASK-023 (Daily/Weekly Leaderboards)
- TASK-036 (Tests E2E)
- TASK-037 → TASK-038 (Docker + CI/CD)
- TASK-039 → TASK-040 (Observability + Docs)

---

## 🔑 TAREAS CRÍTICAS (Camino Crítico)

1. **TASK-006**: Validación de Movimientos (Anti-Cheat) - Core de seguridad
2. **TASK-010**: Game State Manager - Core de lógica
3. **TASK-013**: Event Handlers Socket.io - Core de comunicación
4. **TASK-018**: Auth Middleware Socket.io - Core de seguridad
5. **TASK-027**: GameBoard Component - Core de UI
6. **TASK-029**: Input System - Core de interacción

---

## 📈 MÉTRICAS DE ÉXITO

### Técnicas
- **Cobertura de Tests**: >80% backend, >70% frontend
- **Latencia Socket.io**: <50ms promedio
- **Tick Rate Estable**: 60 FPS en renderizado
- **Zero Trampas**: 100% validación server-side

### Producto
- **Tiempo de Partida**: 3-10 minutos promedio
- **Usuarios Concurrentes**: Soportar 100+ sin degradación
- **Leaderboard**: Actualización en <1 segundo
- **Reconexión**: <3 segundos recuperación de estado

---

## 🏷️ ETIQUETAS UTILIZADAS

- `setup`, `infrastructure`: Configuración inicial
- `backend`, `frontend`: Stack tecnológico
- `game-logic`, `core`: Lógica fundamental
- `socket.io`, `event-handlers`: Comunicación real-time
- `auth`, `security`: Autenticación y seguridad
- `redis`, `database`, `leaderboard`: Persistencia
- `ui`, `game-view`, `input`: Interfaz de usuario
- `testing`, `quality`, `e2e`: Calidad de código
- `devops`, `ci-cd`, `docker`: Operaciones
- `documentation`, `api`: Documentación
- `critical`: Tareas en camino crítico

---

## 📝 NOTAS ADICIONALES

### Decisiones de Arquitectura
1. **Autoridad del Servidor**: Toda la lógica de juego vive en el servidor. El cliente es un "dumb terminal" que solo renderiza.
2. **Anti-Cheat**: Validación exhaustiva de cada movimiento. Logs de intentos sospechosos.
3. **Tick Rate Determinista**: El servidor controla la gravedad, no el cliente.
4. **State Sync**: El servidor envía el estado completo en cada update (no deltas) para simplificar.

### Riesgos Técnicos
- **Latencia de Red**: Mitigar con predicción en cliente (opcional, sprint 6)
- **Escalabilidad**: Empezar con monolito, planear microservicios si >1000 usuarios
- **Redis Downtime**: Implementar fallback a in-memory si Redis falla

### Extensiones Futuras (Post-MVP)
- Modo multijugador competitivo (1v1)
- Skins y customización
- Replay system
- Seasonal rankings
- Mobile app (React Native)

---

**Documento generado**: 2025-12-24  
**Responsable**: Project Manager  
**Versión**: 1.0
