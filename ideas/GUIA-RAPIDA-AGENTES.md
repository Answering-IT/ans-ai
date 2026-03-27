# Guía Rápida: Cómo Definir un Agente de IA

Esta guía te ayuda a completar la plantilla de agentes de IA de forma efectiva.

## Lo Más Importante Primero

Antes de llenar la plantilla completa, responde estas 5 preguntas clave:

1. **¿Qué hace el agente?** (1 línea)
2. **¿Qué recibe como input?** (formato y ejemplo)
3. **¿Qué genera como output?** (formato y ejemplo)
4. **¿Cuál es el prompt/instrucción principal?** (cómo se comporta)
5. **¿Qué herramientas necesita?** (APIs, archivos, etc.)

Con estas 5 respuestas, ya tienes lo esencial para automatizar.

---

## Secciones Críticas de la Plantilla

### 1. Propósito del Agente ⭐⭐⭐
**Por qué es importante**: Define el alcance y evita scope creep.

**Cómo completarlo**:
- Sé específico: "Analiza feedback de clientes" ✓
- Evita vaguedad: "Ayuda con cosas de producto" ✗
- Una línea clara es mejor que un párrafo confuso

### 2. Inputs y Outputs ⭐⭐⭐
**Por qué es importante**: Sin esto, el agente no puede ejecutarse.

**Cómo completarlo**:
- Incluye SIEMPRE un ejemplo real
- Especifica el formato exacto (JSON schema si es posible)
- Piensa en casos edge: ¿qué pasa si el input está vacío?

**Ejemplo bueno**:
```json
Input: {"texto": "string", "fecha": "YYYY-MM-DD"}
Output: {"categoria": "bug|feature|otro", "prioridad": 1-5}
```

**Ejemplo malo**:
```
Input: texto
Output: resultado
```

### 3. Comportamiento del Agente (Prompt) ⭐⭐⭐
**Por qué es importante**: El prompt ES el agente. Sin buen prompt, no funciona.

**Cómo completarlo**:
- Escribe como si le hablaras a una persona inteligente
- Sé explícito sobre lo que NO debe hacer
- Incluye ejemplos dentro del prompt si es complejo
- Define el formato de respuesta esperado

**Template de prompt efectivo**:
```
Eres un [ROL] experto en [DOMINIO].

Tu trabajo es:
1. [TAREA 1]
2. [TAREA 2]
3. [TAREA 3]

Reglas importantes:
- SIEMPRE [REGLA 1]
- NUNCA [REGLA 2]
- Si [CONDICIÓN], entonces [ACCIÓN]

Formato de salida:
[ESPECIFICAR FORMATO EXACTO]

Ejemplo:
Input: [EJEMPLO]
Output: [EJEMPLO]
```

### 4. Herramientas y Capacidades ⭐⭐
**Por qué es importante**: Define qué necesitas integrar.

**Cómo completarlo**:
- Lista TODO lo que el agente necesita acceder
- Incluye APIs externas (con sus credenciales)
- Menciona permisos de archivos/sistema
- Piensa en costos (APIs de pago)

### 5. Casos de Uso ⭐⭐
**Por qué es importante**: Valida que el agente realmente resuelve el problema.

**Cómo completarlo**:
- Mínimo 2 casos de uso completos
- Uno simple (happy path)
- Uno con complicaciones
- Incluye tiempos esperados

### 6. Manejo de Errores ⭐
**Por qué es importante**: Los agentes fallan. Necesitan saber qué hacer.

**Cómo completarlo**:
- Lista los 3 errores más probables
- Define qué hacer en cada caso
- ¿Cuándo debe pedir ayuda humana?

---

## Checklist Antes de Enviar la Idea

- [ ] Completé las 5 preguntas clave del inicio
- [ ] Tengo ejemplos REALES de input/output
- [ ] Mi prompt es claro y específico
- [ ] Listé todas las herramientas/APIs necesarias
- [ ] Incluí al menos 2 casos de uso
- [ ] Definí qué hacer cuando algo falla
- [ ] El nombre del archivo es descriptivo: `agente-[nombre].md`

---

## Errores Comunes a Evitar

### ❌ Error 1: Prompts vagos
**Malo**: "Analiza los datos y dame insights"
**Bueno**: "Analiza el CSV, identifica las 3 columnas con más valores nulos, y sugiere estrategias de limpieza"

### ❌ Error 2: Inputs sin formato
**Malo**: "Recibe un archivo con datos"
**Bueno**: "Recibe CSV con columnas: [nombre, email, fecha, comentario]"

### ❌ Error 3: No pensar en errores
**Malo**: [No menciona errores]
**Bueno**: "Si el archivo no existe, enviar email a admin y salir con código 1"

### ❌ Error 4: Agentes muy complejos
**Malo**: "Un agente que hace 10 cosas diferentes"
**Bueno**: "Un agente enfocado en 1-2 tareas específicas"

Regla de oro: **Un agente = Un propósito claro**

### ❌ Error 5: No incluir ejemplos
**Malo**: "Output en JSON"
**Bueno**:
```json
{
  "status": "success",
  "data": {...}
}
```

---

## Consejos para Producto

### 🎯 Empieza simple
No necesitas llenar TODA la plantilla el primer día. Empieza con:
1. Propósito
2. Input/Output con ejemplos
3. Prompt básico
4. 1 caso de uso

El resto puede completarse después con ayuda del equipo técnico.

### 🎯 Piensa en automatización
Pregúntate: "Si esto fuera automático, ¿qué decisiones necesita tomar?"
- ¿Cuándo ejecutarse?
- ¿A quién notificar?
- ¿Dónde guardar resultados?

### 🎯 Usa ejemplos reales
No inventes datos ficticios. Usa ejemplos reales (anonimizados) de tu día a día.

### 🎯 Itera
El primer prompt nunca es perfecto. Está bien hacer varias versiones.

---

## Flujo Recomendado

```
1. Identifica tarea repetitiva
   ↓
2. Copia TEMPLATE-AGENTE-IA.md
   ↓
3. Llena las 5 preguntas clave
   ↓
4. Escribe 1 ejemplo completo
   ↓
5. Escribe el prompt principal
   ↓
6. Guarda y comparte con el equipo
   ↓
7. Desarrollo crea prototipo
   ↓
8. Pruebas con datos reales
   ↓
9. Itera hasta que funcione
   ↓
10. Automatiza por completo
```

---

## Preguntas Frecuentes

**P: ¿Cuánto detalle necesito?**
R: Suficiente para que alguien técnico pueda implementarlo sin preguntarte nada.

**P: ¿Qué pasa si no sé qué API usar?**
R: Describe qué necesitas lograr. El equipo técnico te ayudará con el "cómo".

**P: ¿Todos los agentes necesitan APIs externas?**
R: No. Algunos solo procesan archivos localmente.

**P: ¿Puedo crear un agente que haga muchas cosas?**
R: Mejor crear varios agentes simples que uno complejo.

**P: ¿Cómo sé si mi prompt es bueno?**
R: Si puedes dárselo a un colega y entiende exactamente qué hacer, es bueno.

---

## Recursos Adicionales

- Ver `agente-ejemplo-analizador-feedback.md` para un ejemplo completo
- Consultar con el equipo técnico para validar viabilidad
- Revisar agentes existentes en `/agentes` para inspiración

---

## Contacto

Si tienes dudas completando la plantilla:
- Slack: #producto-agentes
- Pair con: [Desarrollador Senior]
- Wiki: [Link a documentación interna]
