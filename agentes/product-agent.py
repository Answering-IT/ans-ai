#!/usr/bin/env python3
"""
Product Agent - Agente de Producto
Genera prototipos funcionales a partir de ideas documentadas

Este agente:
1. Lee un archivo de idea desde /ideas
2. Extrae requerimientos y funcionalidades
3. Genera plan de desarrollo
4. Propone arquitectura
5. Crea prototipo funcional en /prototipos
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path

def read_idea_file(filepath):
    """Lee y parsea el archivo de idea"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Archivo no encontrado: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parsear contenido markdown
    # En una implementación real, esto sería más sofisticado
    return {
        'content': content,
        'name': Path(filepath).stem,
        'timestamp': datetime.now().isoformat()
    }

def analyze_requirements(idea):
    """Analiza requerimientos de la idea"""
    print(f"\n📋 Analizando idea: {idea['name']}")
    print("=" * 50)

    # Aquí iría la lógica de análisis con LLM
    # Por ahora, estructura básica

    requirements = {
        'project_name': idea['name'],
        'features': [],
        'tech_stack': ['Python', 'Flask', 'JSON'],
        'complexity': 'medium'
    }

    return requirements

def generate_architecture(requirements):
    """Genera propuesta de arquitectura"""
    print("\n🏗️  Generando arquitectura...")

    architecture = {
        'type': 'monolithic_api',
        'components': [
            'API REST',
            'Capa de negocio',
            'Persistencia JSON'
        ],
        'structure': {
            'main.py': 'Punto de entrada',
            'api/': 'Endpoints REST',
            'models/': 'Modelos de datos',
            'data/': 'Archivos JSON'
        }
    }

    return architecture

def create_prototype(requirements, architecture):
    """Crea el prototipo funcional"""
    project_name = requirements['project_name']
    prototype_dir = Path(__file__).parent.parent / 'prototipos' / project_name

    print(f"\n🚀 Creando prototipo en: {prototype_dir}")

    # Crear estructura de directorios
    prototype_dir.mkdir(parents=True, exist_ok=True)
    (prototype_dir / 'data').mkdir(exist_ok=True)
    (prototype_dir / 'api').mkdir(exist_ok=True)
    (prototype_dir / 'models').mkdir(exist_ok=True)

    # Crear archivos base
    create_readme(prototype_dir, requirements)
    create_main_file(prototype_dir, requirements)
    create_requirements_file(prototype_dir)
    create_sample_data(prototype_dir / 'data')

    print(f"✅ Prototipo creado exitosamente")
    print(f"\nPara ejecutar:")
    print(f"  cd prototipos/{project_name}")
    print(f"  pip install -r requirements.txt")
    print(f"  python main.py")

    return prototype_dir

def create_readme(directory, requirements):
    """Crea README del prototipo"""
    content = f"""# {requirements['project_name']}

**Fecha de Creación**: {datetime.now().strftime('%Y-%m-%d')}
**Tipo**: Prototipo MVP
**Estado**: Funcional Local

## Descripción

Prototipo generado automáticamente por Product Agent.

## Tecnologías

- Python 3.x
- Flask (API REST)
- JSON (Persistencia)

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

El servidor estará disponible en `http://localhost:5000`

## Endpoints API

- `GET /` - Información del API
- `GET /api/items` - Listar items
- `POST /api/items` - Crear item
- `GET /api/items/<id>` - Obtener item
- `PUT /api/items/<id>` - Actualizar item
- `DELETE /api/items/<id>` - Eliminar item

## Estructura de Datos

Los datos se almacenan en `data/items.json` en formato JSON.

Estructura de un item:
```json
{{
  "id": "uuid",
  "name": "string",
  "created_at": "timestamp"
}}
```

## Próximos Pasos

- [ ] Agregar validaciones
- [ ] Implementar más endpoints
- [ ] Agregar tests
- [ ] UI básica

## Changelog

Ver actualizaciones en `/CHANGELOG.md` del repositorio principal.
"""

    with open(directory / 'README.md', 'w', encoding='utf-8') as f:
        f.write(content)

def create_main_file(directory, requirements):
    """Crea archivo principal del prototipo"""
    content = '''#!/usr/bin/env python3
"""
Prototipo MVP - API REST con persistencia JSON
Generado por Product Agent
"""

from flask import Flask, jsonify, request
import json
import uuid
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path(__file__).parent / 'data' / 'items.json'

def load_data():
    """Carga datos desde JSON"""
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(data):
    """Guarda datos en JSON"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    """Información del API"""
    return jsonify({
        'name': 'Prototipo MVP API',
        'version': '1.0.0',
        'endpoints': [
            'GET /api/items',
            'POST /api/items',
            'GET /api/items/<id>',
            'PUT /api/items/<id>',
            'DELETE /api/items/<id>'
        ]
    })

@app.route('/api/items', methods=['GET'])
def get_items():
    """Listar todos los items"""
    items = load_data()
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def create_item():
    """Crear nuevo item"""
    data = request.get_json()

    item = {
        'id': str(uuid.uuid4()),
        'name': data.get('name', ''),
        'created_at': datetime.now().isoformat()
    }

    items = load_data()
    items.append(item)
    save_data(items)

    return jsonify(item), 201

@app.route('/api/items/<item_id>', methods=['GET'])
def get_item(item_id):
    """Obtener item por ID"""
    items = load_data()
    item = next((i for i in items if i['id'] == item_id), None)

    if item:
        return jsonify(item)
    return jsonify({'error': 'Item no encontrado'}), 404

@app.route('/api/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    """Actualizar item"""
    items = load_data()
    item = next((i for i in items if i['id'] == item_id), None)

    if not item:
        return jsonify({'error': 'Item no encontrado'}), 404

    data = request.get_json()
    item.update(data)
    item['updated_at'] = datetime.now().isoformat()

    save_data(items)
    return jsonify(item)

@app.route('/api/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Eliminar item"""
    items = load_data()
    items = [i for i in items if i['id'] != item_id]
    save_data(items)

    return jsonify({'message': 'Item eliminado'})

if __name__ == '__main__':
    # Crear archivo de datos si no existe
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        save_data([])

    print("🚀 Servidor iniciando en http://localhost:5000")
    print("📚 Ver README.md para documentación de endpoints")
    app.run(debug=True, port=5000)
'''

    with open(directory / 'main.py', 'w', encoding='utf-8') as f:
        f.write(content)

    # Hacer ejecutable
    os.chmod(directory / 'main.py', 0o755)

def create_requirements_file(directory):
    """Crea archivo de dependencias"""
    content = """Flask==3.0.0
"""

    with open(directory / 'requirements.txt', 'w', encoding='utf-8') as f:
        f.write(content)

def create_sample_data(data_dir):
    """Crea datos de ejemplo"""
    sample_data = []

    with open(data_dir / 'items.json', 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=2)

def update_changelog(prototype_name):
    """Actualiza el CHANGELOG principal"""
    changelog_file = Path(__file__).parent.parent / 'CHANGELOG.md'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')

    entry = f"""
## [{timestamp}] - Prototipo {prototype_name}

### Agregado
- Nuevo prototipo generado: {prototype_name}
- Estructura base con API REST
- Persistencia en JSON
- README con documentación

"""

    # Leer contenido actual
    with open(changelog_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insertar nueva entrada después de [Unreleased]
    parts = content.split('## [Unreleased]')
    if len(parts) == 2:
        new_content = parts[0] + '## [Unreleased]' + parts[1].split('\n---\n')[0] + '\n---\n' + entry + parts[1].split('\n---\n')[1]
    else:
        new_content = content + entry

    with open(changelog_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"📝 CHANGELOG.md actualizado")

def main(idea_filepath):
    """Flujo principal del agente"""
    try:
        print("🤖 Product Agent - Generador de Prototipos")
        print("=" * 50)

        # 1. Leer idea
        idea = read_idea_file(idea_filepath)

        # 2. Analizar requerimientos
        requirements = analyze_requirements(idea)

        # 3. Generar arquitectura
        architecture = generate_architecture(requirements)

        # 4. Crear prototipo
        prototype_dir = create_prototype(requirements, architecture)

        # 5. Actualizar changelog
        update_changelog(requirements['project_name'])

        print("\n✨ Proceso completado exitosamente")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python product-agent.py <archivo-idea>")
        print("Ejemplo: python product-agent.py ideas/mi-idea.md")
        sys.exit(1)

    main(sys.argv[1])
