# 📖 Guía Rápida del Project Manager

## 🎯 Resumen Ejecutivo

Proyecto: **Tetris Autoritario**  
Objetivo: Sistema Tetris con control total del servidor, anti-cheat, JWT auth, y Redis leaderboard  
Duración: **5 semanas (186 horas)**  
Equipo Recomendado: **2 desarrolladores** (1 backend, 1 frontend)

---

## 📋 Documentos Clave

| Documento | Propósito | Cuándo Usar |
|-----------|-----------|-------------|
| **PROJECT_PLAN.md** | Plan técnico detallado | Planificación inicial, referencia técnica |
| **TRELLO_BOARD.md** | Board visual estilo Trello | Daily standups, tracking de progreso |
| **issues/TETRIS_ISSUES.json** | Formato importable | Importar a herramientas (Trello/Jira) |
| **README.md** | Overview del proyecto | Onboarding de equipo, presentaciones |

---

## 🎯 Tareas Críticas (Camino Crítico)

Estas **9 tareas** bloquean el resto del proyecto. Priorizar asignación:

1. **TASK-004**: Matriz 10x20 → Base de todo el juego
2. **TASK-006**: Validación Anti-Cheat → Seguridad core
3. **TASK-010**: Game State Manager → Integración backend
4. **TASK-013**: Event Handlers Socket.io → Comunicación
5. **TASK-017**: Endpoints Auth → Login de usuarios
6. **TASK-018**: Auth Middleware Socket.io → Seguridad
7. **TASK-021**: Leaderboard Sorted Sets → Scoring
8. **TASK-027**: GameBoard Component → UI principal
9. **TASK-029**: Input System → Interacción usuario

**Acción**: Asignar estas tareas primero a developers senior.

---

## 📅 Plan de Sprints (5 Semanas)

### Sprint 1: Fundamentos (Semana 1)
**Objetivo**: Setup + Game Logic Core + Auth  
**Entregables**:
- Monorepo configurado
- Matriz 10x20 funcionando
- Tetrominos con rotaciones
- Validación anti-cheat básica
- Endpoints de login/register

**Riesgos**: 
- Complejidad del SRS (Super Rotation System)
- Configuración de TypeScript strict mode

**Mitigación**: Reservar 2h extra para debugging de rotaciones

---

### Sprint 2: Backend Completo (Semana 2)
**Objetivo**: Game Logic + Socket.io + Redis  
**Entregables**:
- Scoring y niveles
- Tick rate de caída
- Socket.io server con rooms
- Event handlers (move, rotate, drop)
- Redis leaderboard básico

**Riesgos**: 
- Rate limiting de acciones (performance)
- Sincronización de estado

**Mitigación**: Tests de carga con 50+ usuarios simulados

---

### Sprint 3: Frontend Completo (Semana 3)
**Objetivo**: UI Funcional + Integración  
**Entregables**:
- Auth middleware Socket.io (CRÍTICO)
- Login/Register UI
- GameBoard component
- Input system (teclado)
- API de leaderboard

**Riesgos**: 
- Latencia en la comunicación
- Sincronización de animaciones

**Mitigación**: Implementar predicción cliente-side (opcional)

---

### Sprint 4: Integración (Semana 4)
**Objetivo**: Pulido + Tests  
**Entregables**:
- NextPieces, ScorePanel, GameOver modals
- Leaderboard view completa
- Sistema de reconexión
- Tests unitarios (>80% backend)
- Tests frontend (>70%)

**Riesgos**: 
- Bugs en reconexión
- Baja cobertura de tests

**Mitigación**: Dedicar 1 día completo solo a testing

---

### Sprint 5: DevOps (Semana 5)
**Objetivo**: Deployment + Extras  
**Entregables**:
- Daily/Weekly leaderboards
- Docker + docker-compose
- CI/CD con GitHub Actions
- Tests E2E con Playwright
- Documentación API (Swagger)

**Riesgos**: 
- Complejidad de CI/CD
- TTL de Redis no funcionando

**Mitigación**: Usar templates de GitHub Actions existentes

---

## 👥 Asignación Sugerida (2 Developers)

### Developer Backend (Full-stack con énfasis backend)
**Sprints 1-2 (Focus: Backend Core)**
- TASK-001: Monorepo setup
- TASK-002: Backend base
- TASK-004 a TASK-010: Game logic completo
- TASK-011 a TASK-015: Socket.io
- TASK-016 a TASK-019: Auth
- TASK-020 a TASK-023: Redis

**Sprints 3-5 (Support: Integration + DevOps)**
- TASK-033, TASK-034: Tests backend
- TASK-037, TASK-038: Docker + CI/CD
- TASK-039: Logging

### Developer Frontend (Full-stack con énfasis frontend)
**Sprints 1-2 (Setup + Preparación)**
- TASK-003: Frontend base
- Estudiar documentación Socket.io
- Diseñar wireframes UI

**Sprints 3-4 (Focus: Frontend Complete)**
- TASK-024 a TASK-032: Todo el frontend
- TASK-035: Tests frontend
- TASK-036: Tests E2E

**Sprint 5 (Finalize)**
- TASK-040: Documentación
- Polish UI/UX

---

## 📊 Tracking de Progreso

### Daily Standup Questions
1. ¿Qué tarea completaste ayer? (mover a DONE)
2. ¿En qué tarea trabajas hoy? (mover a DOING)
3. ¿Algún blocker? (identificar dependencias)

### Métricas Semanales
- **Velocity**: Horas completadas vs. planificadas
- **Burndown**: Tareas restantes
- **Bloqueadores**: Tareas críticas no iniciadas
- **Cobertura de Tests**: % alcanzado

### Red Flags 🚩
- ⚠️ Tarea crítica lleva >1.5x tiempo estimado
- ⚠️ Developer con >3 tareas en DOING
- ⚠️ Sprint con <60% tareas completadas
- ⚠️ Cobertura tests <70% en semana 4

---

## 🔧 Herramientas Recomendadas

### Project Management
- **Trello**: Usar columnas TO DO / DOING / DONE
- **GitHub Projects**: Beta con automation
- **Jira**: Para equipos enterprise

### Importación de Tareas
```bash
# Opción 1: GitHub CLI (Crear issues)
cd Tetris
gh issue create --title "TASK-001: Monorepo" \
  --body "$(cat issues/TETRIS_ISSUES.json | jq '.tasks[0]')"

# Opción 2: Trello API
# Ver issues/README.md para script de importación

# Opción 3: Manual
# Copiar/pegar desde TRELLO_BOARD.md
```

### Communication
- **Daily Standups**: 15 min diarios (Zoom/Meet)
- **Sprint Planning**: 2h inicio de sprint
- **Sprint Review**: 1h fin de sprint
- **Retrospective**: 1h fin de sprint

---

## 🎯 Criterios de Aceptación por Sprint

### Sprint 1 ✅
- [ ] `npm run dev` levanta backend
- [ ] Tests de GameBoard pasan
- [ ] Login endpoint devuelve JWT válido
- [ ] Postman collection funcional

### Sprint 2 ✅
- [ ] Cliente conecta a Socket.io con JWT
- [ ] Movimientos de pieza validados server-side
- [ ] Leaderboard API devuelve top 10
- [ ] Redis con 1000+ usuarios no degrada

### Sprint 3 ✅
- [ ] Login UI funcional
- [ ] GameBoard renderiza 10x20
- [ ] Teclas mueven piezas (con lag <50ms)
- [ ] Leaderboard se muestra en UI

### Sprint 4 ✅
- [ ] Partida completa (inicio → game over)
- [ ] Reconexión recupera estado
- [ ] Tests >80% backend, >70% frontend
- [ ] E2E test pasa en CI

### Sprint 5 ✅
- [ ] `docker-compose up` funciona
- [ ] CI ejecuta tests en cada PR
- [ ] Swagger docs completas
- [ ] Deploy a staging exitoso

---

## 🚨 Gestión de Riesgos

### Riesgo 1: Latencia de Red
**Probabilidad**: Media  
**Impacto**: Alto  
**Mitigación**: 
- Optimizar payloads Socket.io
- Throttling a 60 FPS
- (Opcional) Predicción cliente-side

### Riesgo 2: Escalabilidad Redis
**Probabilidad**: Baja  
**Impacto**: Alto  
**Mitigación**: 
- Redis cluster (futuro)
- Fallback a in-memory
- Monitoring con Redis Insights

### Riesgo 3: Anti-Cheat Falsos Positivos
**Probabilidad**: Media  
**Impacto**: Medio  
**Mitigación**: 
- Logs detallados de validaciones
- Replay system (futuro)
- Ajustar tolerancia de rate limiting

### Riesgo 4: Scope Creep
**Probabilidad**: Alta  
**Impacto**: Alto  
**Mitigación**: 
- Mantener MVP claro
- "Nice to have" en backlog separado
- Aprobar cambios solo en retrospective

---

## 📈 Métricas de Éxito del Proyecto

### Al Final del Sprint 5, Debe Cumplirse:

#### Técnicas
- [x] **Tests**: >80% backend, >70% frontend
- [x] **Performance**: Latencia <50ms Socket.io
- [x] **Rendering**: 60 FPS estable
- [x] **Security**: 100% validación server-side
- [x] **CI/CD**: Pipeline verde en GitHub Actions

#### Producto
- [x] **Gameplay**: Partida completa sin bugs críticos
- [x] **Usuarios**: 100+ concurrentes sin degradación
- [x] **Leaderboard**: Actualización <1s
- [x] **Reconexión**: <3s recuperación estado
- [x] **UX**: UI responsive en desktop y móvil

#### Proceso
- [x] **Documentación**: README + Swagger completos
- [x] **Deploy**: docker-compose up funciona
- [x] **Code Quality**: ESLint sin warnings
- [x] **Logs**: Monitoring con Winston configurado

---

## 🎓 Lecciones Aprendidas (Post-Proyecto)

### Qué Salió Bien
- *[Rellenar al final del proyecto]*

### Qué Mejorar
- *[Rellenar al final del proyecto]*

### Recomendaciones para Proyectos Futuros
- *[Rellenar al final del proyecto]*

---

## 📞 Contactos y Recursos

### Documentación Técnica
- **Socket.io**: https://socket.io/docs/v4/
- **Redis Sorted Sets**: https://redis.io/docs/data-types/sorted-sets/
- **JWT Best Practices**: https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html
- **Tetris SRS**: https://tetris.wiki/Super_Rotation_System

### Herramientas
- **Redis Commander**: GUI para Redis
- **Postman**: Testing de API REST
- **Socket.io Admin UI**: https://socket.io/docs/v4/admin-ui/

---

**Última Actualización**: 2025-12-24  
**Versión**: 1.0  
**Responsable**: Project Manager
