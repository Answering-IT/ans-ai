# Ans-AI 🚀

Repositorio organizacional para gestión de proyectos, ideas y prototipos mediante agentes autónomos.

## Estructura

```
ans-ai/
├── agentes/          # Agentes autónomos que automatizan tareas
├── proyectos/        # Proyectos existentes en producción/mantenimiento
├── prototipos/       # MVPs y pruebas de concepto funcionales
├── ideas/            # Ideas de nuevos productos o features
├── CHANGELOG.md      # Histórico de cambios del repositorio
├── CLAUDE.md         # Guía para Claude y el sistema
└── README.md         # Este archivo
```

## Inicio Rápido

### 1. Proponer una Idea
```bash
# Crear nueva idea desde plantilla
cp ideas/TEMPLATE.md ideas/mi-nueva-idea.md
# Editar con tu propuesta
```

### 2. Desarrollar un Prototipo
```bash
# El agente de producto leerá la idea y generará el prototipo
claude run agentes/product-agent.py ideas/mi-nueva-idea.md
```

### 3. Ejecutar un Prototipo
```bash
cd prototipos/nombre-prototipo
python main.py  # o node index.js
```

## Flujo de Trabajo

1. **Ideación**: Producto escribe ideas en `/ideas`
2. **Planificación**: Agente genera plan de desarrollo
3. **Arquitectura**: Agente propone arquitectura técnica
4. **Prototipado**: Agente crea MVP funcional
5. **Validación**: Equipo prueba localmente
6. **Iteración**: Mejoras basadas en feedback
7. **Producción**: Transición a `/proyectos` si se aprueba

## Principios

- **Simplicidad**: Prototipos ejecutables sin configuración compleja
- **Accesibilidad**: Usar JSON para que todos puedan entender los datos
- **Documentación**: Todo debe estar documentado
- **Trazabilidad**: Registrar cambios en CHANGELOG.md
- **Colaboración**: Fomentar participación de todo el equipo

## Equipo

- Producto (2)
- Desarrollo (2)
- Infraestructura (1)

## Tecnologías Preferidas para Prototipos

- Python 3.x
- JavaScript/Node.js
- JSON para persistencia
- Frameworks ligeros (Flask, Express)
- Sin bases de datos en prototipos iniciales

## Contribuir

1. Crea tu rama: `git checkout -b feature/nueva-funcionalidad`
2. Documenta cambios en CHANGELOG.md
3. Commit: `git commit -m 'Agregar nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

## Documentación

Para más detalles, consulta:
- [CLAUDE.md](./CLAUDE.md) - Guía completa del repositorio
- [CHANGELOG.md](./CHANGELOG.md) - Histórico de cambios
- Cada carpeta tiene su propio README con información específica

## Licencia

Uso interno de la empresa.
