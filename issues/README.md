# Issues Directory

Este directorio contiene todas las tareas del proyecto en formato individual para fácil importación a herramientas de gestión de proyectos (Trello, Jira, GitHub Projects, etc.).

## Estructura

- **Tareas organizadas por Hito (H1-H8)**
- **Formato JSON para importación automática**
- **Cada archivo contiene metadatos completos**

## Importar a Trello

1. Usar la API de Trello con los archivos JSON
2. O crear manualmente copiando el contenido

## Importar a GitHub Projects

```bash
# Usar GitHub CLI para crear issues
gh issue create --title "TASK-001: Inicializar Monorepo" --body "$(cat H1-TASK-001.md)"
```

## Importar a Jira

1. Exportar JSON a CSV
2. Usar la funcionalidad de importación masiva de Jira

## Flujo de Trabajo Sugerido

1. **TO DO**: Tareas que están listas para iniciar
2. **DOING**: Tareas en progreso (máx 3 por desarrollador)
3. **DONE**: Tareas completadas y validadas
