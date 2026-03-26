# Ans-AI - Repositorio Organizacional

## Propósito del Repositorio

Este repositorio es el centro de operaciones de nuestra empresa. Contiene documentación, proyectos, ideas y prototipos organizados para facilitar la colaboración y el desarrollo ágil mediante agentes autónomos.

## Estructura del Repositorio

```
ans-ai/
├── agentes/          # Agentes autónomos que automatizan tareas
├── proyectos/        # Proyectos existentes en producción/mantenimiento
├── prototipos/       # MVPs y pruebas de concepto funcionales
├── ideas/            # Ideas de nuevos productos o features
├── CHANGELOG.md      # Histórico de cambios del repositorio
└── CLAUDE.md         # Este archivo - guía para Claude
```

## Estructura del Equipo

- **Producto**: 2 personas
- **Desarrollo**: 2 personas (1 senior/arquitectura, 1 front-end)
- **Infraestructura**: 1 persona

## Filosofía de Trabajo

### Prototipos
- Los prototipos deben ser funcionales localmente
- Usar JSON para persistencia (accesible para personas no técnicas)
- Tecnologías preferidas: Python, JavaScript/Node.js
- Cada prototipo debe incluir README.md con instrucciones de ejecución

### Workflow con Agentes
1. Persona de producto escribe idea en `/ideas`
2. Agente lee el requerimiento y crea plan de desarrollo
3. Agente propone arquitectura
4. Agente genera prototipo funcional en `/prototipos`

## Cómo Usar Este Repositorio

### Para Producto
- Crea nuevas ideas en `/ideas/nombre-idea.md`
- Usa la plantilla de ideas (ver `/ideas/TEMPLATE.md`)
- Para features de productos existentes, referenciar el proyecto

### Para Desarrollo
- Revisa prototipos en `/prototipos`
- Documentación de proyectos existentes en `/proyectos`
- Ejecuta agentes desde `/agentes` según sea necesario

### Para Infraestructura
- Mantén actualizada la documentación en `/proyectos`
- Revisa requisitos de deployment en prototipos

## Comandos Útiles

```bash
# Ejecutar agente de producto (desarrollar MVP desde idea)
claude run agentes/product-agent.py ideas/mi-idea.md

# Ver histórico de cambios
cat CHANGELOG.md
```

## Reglas de Contribución

1. Todo cambio debe registrarse en CHANGELOG.md
2. Cada proyecto/prototipo debe tener su propio README.md
3. Usar nomenclatura descriptiva en carpetas y archivos
4. Prototipos deben ser ejecutables localmente sin configuración compleja
5. Ideas deben ser claras y detalladas

## Contacto y Soporte

Para dudas sobre el repositorio, contactar al equipo de desarrollo.
