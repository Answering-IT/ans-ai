# Agentes

Esta carpeta contiene los agentes autónomos que automatizan tareas del repositorio.

## Agentes Disponibles

### 1. Product Agent (product-agent.py)
**Propósito**: Lee ideas de productos y genera prototipos funcionales

**Funcionalidad**:
- Lee archivo de idea desde `/ideas`
- Analiza requerimientos
- Genera plan de desarrollo
- Propone arquitectura técnica
- Crea prototipo funcional en `/prototipos`

**Uso**:
```bash
python agentes/product-agent.py ideas/mi-idea.md
```

### 2. Project Analyzer (Futuro)
Analiza proyectos existentes y genera documentación automática

### 3. Changelog Updater (Futuro)
Actualiza CHANGELOG.md automáticamente basado en commits

## Cómo Funcionan los Agentes

Los agentes son scripts que:
1. Leen archivos de entrada (ideas, proyectos, etc.)
2. Procesan la información usando LLMs o lógica programada
3. Generan outputs (código, documentación, planes)
4. Actualizan el repositorio automáticamente

## Tecnologías

- Python 3.x para agentes principales
- OpenAI API / Anthropic API para procesamiento de lenguaje
- Librerías: langchain, openai, anthropic

## Configuración

Cada agente puede requerir:
- Variables de entorno (API keys)
- Archivo de configuración
- Dependencias específicas

Ver README de cada agente para detalles.

## Crear un Nuevo Agente

1. Crea archivo `nombre-agente.py`
2. Implementa funcionalidad usando template
3. Documenta en este README
4. Agrega tests si es posible
5. Actualiza CHANGELOG.md

## Template de Agente

```python
#!/usr/bin/env python3
"""
Nombre del Agente
Descripción de lo que hace
"""

import sys
import os

def main(input_file):
    # Leer input
    # Procesar
    # Generar output
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python agente.py <archivo-entrada>")
        sys.exit(1)

    main(sys.argv[1])
```

## Mejores Prácticas

- Manejar errores gracefully
- Loggear acciones importantes
- Validar inputs
- Generar outputs bien formateados
- Actualizar CHANGELOG.md automáticamente
