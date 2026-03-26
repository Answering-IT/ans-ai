# Prototipos

Esta carpeta contiene MVPs y pruebas de concepto funcionales de nuevos productos o features.

## Características de un Prototipo

- **Funcional localmente**: Debe ejecutarse sin configuración compleja
- **Usa JSON**: Para persistencia de datos (accesible para no-técnicos)
- **Bien documentado**: README con instrucciones claras
- **Tecnologías simples**: Python, Node.js, frameworks ligeros
- **Sin bases de datos**: En fase de prototipo, usar JSON

## Estructura de un Prototipo

```
nombre-prototipo/
├── README.md          # Documentación del prototipo
├── main.py            # Archivo principal (o index.js)
├── requirements.txt   # Dependencias Python
├── package.json       # Dependencias Node.js
├── data/             # Carpeta para archivos JSON
│   └── *.json
├── src/              # Código fuente organizado
└── docs/             # Documentación adicional
```

## Ejecutar un Prototipo

### Python
```bash
cd prototipos/nombre-prototipo
pip install -r requirements.txt
python main.py
```

### Node.js
```bash
cd prototipos/nombre-prototipo
npm install
npm start
```

## Del Prototipo a Producción

Cuando un prototipo se aprueba para producción:
1. Se crea proyecto completo en `/proyectos`
2. Se migra a repositorio GitHub propio
3. Se implementa base de datos real
4. Se configura infraestructura
5. El prototipo permanece aquí como referencia

## Prototipos Actuales

<!-- Lista de prototipos activos -->
- Ninguno aún

## Changelog de Prototipos

Cada actualización a un prototipo debe:
1. Documentarse en su propio README
2. Registrarse en `/CHANGELOG.md` principal
3. Actualizar la fecha de última modificación
