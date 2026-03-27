# [Nombre del Agente de IA]

**Fecha**: YYYY-MM-DD
**Autor**: [Nombre]
**Tipo**: Agente Autónomo de IA
**Prioridad**: [ ] Alta | [ ] Media | [ ] Baja

---

## 1. Propósito del Agente

### Descripción en una línea
[¿Qué hace este agente en 1-2 líneas?]

### Problema que Resuelve
[¿Qué problema específico automatiza o resuelve este agente?]

### Valor para el Usuario
[¿Cómo beneficia a los usuarios o al equipo?]

---

## 2. Inputs y Outputs

### Inputs (Entradas)
**Formato de entrada**: [ ] Texto | [ ] Archivo | [ ] JSON | [ ] API | [ ] Base de datos

**Descripción detallada**:
- Input 1: [Descripción y formato]
- Input 2: [Descripción y formato]

**Ejemplo de input**:
```
[Ejemplo concreto de cómo se ve el input]
```

### Outputs (Salidas)
**Formato de salida**: [ ] Texto | [ ] Archivo | [ ] JSON | [ ] API | [ ] Email | [ ] Notificación

**Descripción detallada**:
- Output 1: [Descripción y formato]
- Output 2: [Descripción y formato]

**Ejemplo de output**:
```
[Ejemplo concreto de cómo se ve el output]
```

---

## 3. Comportamiento del Agente

### Rol del Agente
[Define el rol/personalidad: ej. "Actúa como un analista de datos experto", "Eres un asistente de producto", etc.]

### Instrucciones Base (Prompt Principal)
```
[Escribe aquí las instrucciones principales que el agente debe seguir.
Sé específico sobre:
- Qué debe hacer
- Cómo debe hacerlo
- Qué NO debe hacer
- Restricciones importantes
- Formato de respuesta esperado]
```

### Reglas y Restricciones
1. **Regla 1**: [Ej. "Nunca eliminar información sin confirmación"]
2. **Regla 2**: [Ej. "Siempre validar datos antes de procesarlos"]
3. **Regla 3**: [Ej. "Máximo 3 intentos antes de escalar a humano"]

### Tono y Estilo
- [ ] Formal
- [ ] Casual
- [ ] Técnico
- [ ] Amigable
- [ ] Conciso
- [ ] Detallado

---

## 4. Flujo de Trabajo

### Paso a Paso
Describe el flujo completo del agente:

1. **Recibir Input**
   - ¿De dónde viene?
   - ¿Cómo se valida?

2. **Procesamiento**
   - ¿Qué análisis hace?
   - ¿Qué decisiones toma?
   - ¿Usa APIs externas?

3. **Generación de Output**
   - ¿Qué genera?
   - ¿En qué formato?
   - ¿Dónde lo guarda/envía?

4. **Acciones Posteriores**
   - ¿Actualiza algo?
   - ¿Notifica a alguien?
   - ¿Registra logs?

### Diagrama de Flujo (Opcional)
```
[Input] → [Validación] → [Procesamiento] → [Generación] → [Output]
              ↓               ↓                 ↓
         [Log Error]     [Consulta API]    [Guardar]
```

---

## 5. Capacidades y Herramientas

### Herramientas que Necesita
Marca las herramientas que el agente debe poder usar:

- [ ] **Lectura de archivos**: [Tipos de archivo]
- [ ] **Escritura de archivos**: [Tipos de archivo]
- [ ] **APIs externas**: [Cuáles: OpenAI, Anthropic, Google, etc.]
- [ ] **Base de datos**: [Lectura/Escritura]
- [ ] **Email**: [Envío/Lectura]
- [ ] **Web scraping**: [URLs específicas]
- [ ] **Ejecutar código**: [Python, JavaScript, Bash]
- [ ] **Búsqueda web**: [Google, Bing]
- [ ] **Calendario**: [Crear eventos, consultar]
- [ ] **Notificaciones**: [Slack, Discord, etc.]
- [ ] **Git**: [Commits, PRs, etc.]

### Integraciones Necesarias
- Servicio 1: [Nombre y propósito]
- Servicio 2: [Nombre y propósito]
- API Key requerida: [Sí/No]

### Permisos Requeridos
- [ ] Lectura de archivos del sistema
- [ ] Escritura de archivos del sistema
- [ ] Acceso a internet
- [ ] Ejecución de comandos
- [ ] Acceso a base de datos
- [ ] Acceso a servicios externos

---

## 6. Casos de Uso

### Caso de Uso 1: [Nombre del Caso]
**Usuario**: [Quién lo usa]
**Escenario**: [Contexto]
**Input**: [Qué proporciona el usuario]
**Proceso**: [Qué hace el agente]
**Output**: [Qué recibe el usuario]
**Tiempo esperado**: [Cuánto tarda]

### Caso de Uso 2: [Nombre del Caso]
**Usuario**: [Quién lo usa]
**Escenario**: [Contexto]
**Input**: [Qué proporciona el usuario]
**Proceso**: [Qué hace el agente]
**Output**: [Qué recibe el usuario]
**Tiempo esperado**: [Cuánto tarda]

### Caso de Uso 3: [Nombre del Caso]
[Agregar más según sea necesario]

---

## 7. Manejo de Errores

### Errores Comunes y Soluciones
1. **Error**: [Tipo de error]
   - **Causa**: [Por qué ocurre]
   - **Solución**: [Qué debe hacer el agente]

2. **Error**: [Tipo de error]
   - **Causa**: [Por qué ocurre]
   - **Solución**: [Qué debe hacer el agente]

### Escalación a Humano
¿Cuándo debe el agente pedir ayuda humana?
- Situación 1: [Descripción]
- Situación 2: [Descripción]

### Logs y Monitoreo
- [ ] Registrar todas las ejecuciones
- [ ] Registrar solo errores
- [ ] Notificar al equipo en caso de falla
- [ ] Dashboard de monitoreo

---

## 8. Contexto y Memoria

### ¿Necesita mantener contexto entre ejecuciones?
- [ ] Sí
- [ ] No

Si sí, ¿qué debe recordar?
- Memoria 1: [Qué información]
- Memoria 2: [Qué información]

### ¿Dónde se almacena el contexto?
- [ ] JSON local
- [ ] Base de datos
- [ ] Cache en memoria
- [ ] Otro: [Especificar]

---

## 9. Criterios de Éxito

### Métricas de Desempeño
- **Precisión**: [Ej. 95% de outputs correctos]
- **Velocidad**: [Ej. < 5 segundos por ejecución]
- **Confiabilidad**: [Ej. 99% uptime]

### Criterios de Aceptación
- [ ] Criterio 1: [Descripción]
- [ ] Criterio 2: [Descripción]
- [ ] Criterio 3: [Descripción]

### Pruebas Necesarias
1. Test 1: [Descripción de la prueba]
2. Test 2: [Descripción de la prueba]
3. Test 3: [Descripción de la prueba]

---

## 10. Configuración y Deployment

### Variables de Entorno
```env
AGENTE_API_KEY=
AGENTE_MODEL=claude-3-sonnet
AGENTE_TEMPERATURE=0.7
AGENTE_MAX_TOKENS=4000
```

### Cómo Ejecutarlo
```bash
# Comando para ejecutar el agente
python agentes/nombre-agente.py input.json
```

### Frecuencia de Ejecución
- [ ] Manual (on-demand)
- [ ] Cada hora
- [ ] Diario
- [ ] Semanal
- [ ] Trigger por evento: [Especificar]

### Dónde Corre
- [ ] Local
- [ ] Servidor
- [ ] Cloud (Lambda, Cloud Functions)
- [ ] Contenedor (Docker)

---

## 11. Ejemplos Completos

### Ejemplo 1: Ejecución Exitosa
**Input**:
```json
{
  "campo1": "valor1",
  "campo2": "valor2"
}
```

**Proceso interno del agente**:
```
1. Valida input
2. Consulta API X
3. Procesa datos
4. Genera output
```

**Output**:
```json
{
  "resultado": "éxito",
  "data": {...}
}
```

### Ejemplo 2: Manejo de Error
**Input**:
```json
{
  "campo1": "valor_invalido"
}
```

**Output**:
```json
{
  "error": "Campo1 debe ser numérico",
  "codigo": "VALIDATION_ERROR"
}
```

---

## 12. Iteraciones Futuras

### Features Deseables (No MVP)
- [ ] Feature 1: [Descripción]
- [ ] Feature 2: [Descripción]
- [ ] Feature 3: [Descripción]

### Mejoras Potenciales
- Mejora 1: [Descripción]
- Mejora 2: [Descripción]

---

## 13. Referencias y Recursos

### Documentación Relevante
- [Link a docs de API]
- [Link a ejemplos similares]
- [Link a referencias técnicas]

### Agentes Similares
- Agente X: [En qué se parece]
- Agente Y: [Qué podemos reutilizar]

### Inspiración
- [Productos o herramientas que inspiraron esta idea]

---

## 14. Notas Adicionales

[Cualquier otra información relevante que no encaje en las secciones anteriores]

---

## 15. Checklist para Desarrollo

Para el equipo de desarrollo, antes de considerar el agente completo:

- [ ] Prompt principal definido y testeado
- [ ] Todas las herramientas integradas
- [ ] Manejo de errores implementado
- [ ] Logs configurados
- [ ] Tests escritos y pasando
- [ ] Documentación actualizada
- [ ] Variables de entorno documentadas
- [ ] Ejemplo de uso incluido
- [ ] README del agente creado
- [ ] Registrado en CHANGELOG.md
