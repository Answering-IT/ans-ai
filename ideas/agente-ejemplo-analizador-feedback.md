# Agente Analizador de Feedback de Clientes

**Fecha**: 2026-03-26
**Autor**: Equipo de Producto
**Tipo**: Agente Autónomo de IA
**Prioridad**: [x] Alta | [ ] Media | [ ] Baja

---

## 1. Propósito del Agente

### Descripción en una línea
Analiza automáticamente feedback de clientes y genera reportes con insights accionables.

### Problema que Resuelve
El equipo de producto recibe feedback disperso de múltiples canales (email, Slack, encuestas) y no tiene tiempo para analizar todo manualmente. Se pierden insights importantes y no hay visibilidad clara de tendencias.

### Valor para el Usuario
- Ahorra 10+ horas semanales de análisis manual
- Identifica problemas críticos automáticamente
- Prioriza features basado en demanda real
- Genera reportes ejecutivos listos para usar

---

## 2. Inputs y Outputs

### Inputs (Entradas)
**Formato de entrada**: [x] Archivo | [x] JSON | [x] API

**Descripción detallada**:
- Input 1: Archivo CSV con feedback exportado de sistema de tickets
- Input 2: Mensajes de Slack del canal #customer-feedback
- Input 3: Respuestas de encuestas NPS en formato JSON

**Ejemplo de input**:
```json
{
  "fuente": "slack",
  "fecha": "2026-03-26",
  "mensajes": [
    {
      "usuario": "cliente@example.com",
      "texto": "Sería genial poder exportar los reportes en PDF",
      "timestamp": "2026-03-26T10:30:00Z"
    }
  ]
}
```

### Outputs (Salidas)
**Formato de salida**: [x] Archivo | [x] JSON | [x] Email

**Descripción detallada**:
- Output 1: Reporte markdown con análisis semanal
- Output 2: JSON con temas priorizados y su frecuencia
- Output 3: Email automático al equipo de producto con highlights

**Ejemplo de output**:
```markdown
# Análisis de Feedback - Semana 12, 2026

## Top 3 Solicitudes
1. **Export a PDF** (12 menciones, 8 clientes únicos)
2. **Dark mode** (8 menciones, 6 clientes únicos)
3. **Integraciones con Salesforce** (5 menciones, 5 clientes únicos)

## Bugs Críticos
- Login timeout en móvil (reportado por 4 clientes)

## Sentimiento General
- Positivo: 65%
- Neutral: 25%
- Negativo: 10%
```

---

## 3. Comportamiento del Agente

### Rol del Agente
Actúa como un Product Analyst experto que comprende patrones en feedback de usuarios, identifica tendencias, y comunica insights de forma clara y accionable.

### Instrucciones Base (Prompt Principal)
```
Eres un Product Analyst experto especializado en análisis de feedback de clientes.

Tu trabajo es:
1. Analizar todo el feedback recibido de múltiples fuentes
2. Identificar temas y patrones recurrentes
3. Categorizar por tipo: Feature Request, Bug, Mejora, Queja, Elogio
4. Priorizar basado en:
   - Frecuencia de mención
   - Número de clientes únicos
   - Impacto potencial en el negocio
   - Urgencia (especialmente para bugs)
5. Extraer citas textuales representativas
6. Analizar sentimiento general
7. Generar reporte estructurado y accionable

Reglas importantes:
- Agrupa solicitudes similares (ej. "exportar PDF", "descargar como PDF", "generar PDF" son lo mismo)
- Distingue entre lo que clientes dicen y lo que realmente necesitan
- Identifica bugs críticos que afecten funcionalidad core
- Mantén un tono objetivo y basado en datos
- Siempre incluye evidencia (citas) para cada insight
```

### Reglas y Restricciones
1. **Privacidad**: Nunca incluir información personal identificable en reportes
2. **Deduplicación**: Contar clientes únicos, no solo menciones
3. **Contexto**: No sacar conclusiones sin suficiente evidencia (mínimo 3 menciones)
4. **Urgencia**: Bugs que afecten login, pagos o datos siempre son prioridad 1
5. **Balance**: Incluir tanto positivo como negativo en los reportes

### Tono y Estilo
- [x] Formal
- [ ] Casual
- [x] Técnico
- [ ] Amigable
- [x] Conciso
- [x] Detallado

---

## 4. Flujo de Trabajo

### Paso a Paso

1. **Recibir Input**
   - Lee archivos CSV, JSON de múltiples fuentes
   - Valida que los datos tengan campos requeridos (fecha, texto, fuente)

2. **Procesamiento**
   - Limpia y normaliza textos
   - Extrae temas usando análisis semántico
   - Clasifica cada pieza de feedback por categoría
   - Agrupa similares usando embeddings
   - Analiza sentimiento por pieza
   - Cuenta frecuencias y clientes únicos

3. **Generación de Output**
   - Genera reporte markdown estructurado
   - Crea JSON con datos estructurados para dashboard
   - Identifica top 5 prioridades

4. **Acciones Posteriores**
   - Guarda reporte en `/prototipos/feedback-analyzer/reports/`
   - Envía email al equipo de producto
   - Registra ejecución en log

### Diagrama de Flujo
```
[CSVs/JSONs] → [Validación] → [Limpieza] → [Clasificación] → [Análisis]
                    ↓              ↓             ↓               ↓
               [Log Error]    [Normalizar]  [Agrupar]    [Sentimiento]
                                                              ↓
                                                         [Priorizar]
                                                              ↓
                                                [Generar Reporte + Email]
```

---

## 5. Capacidades y Herramientas

### Herramientas que Necesita

- [x] **Lectura de archivos**: CSV, JSON, TXT
- [x] **Escritura de archivos**: Markdown, JSON
- [x] **APIs externas**: Anthropic Claude (análisis), Slack API (lectura)
- [ ] **Base de datos**: No en MVP
- [x] **Email**: Envío de reportes
- [ ] **Web scraping**: No
- [ ] **Ejecutar código**: Python para procesamiento
- [ ] **Búsqueda web**: No
- [ ] **Calendario**: No
- [x] **Notificaciones**: Slack (opcional)
- [ ] **Git**: No

### Integraciones Necesarias
- **Anthropic API**: Para análisis semántico y clasificación
- **Slack API**: Para leer mensajes del canal #customer-feedback
- **Email (SMTP)**: Para enviar reportes automáticos

### Permisos Requeridos
- [x] Lectura de archivos del sistema
- [x] Escritura de archivos del sistema
- [x] Acceso a internet (APIs)
- [ ] Ejecución de comandos
- [ ] Acceso a base de datos
- [x] Acceso a servicios externos (Slack, Email)

---

## 6. Casos de Uso

### Caso de Uso 1: Análisis Semanal Automático
**Usuario**: Product Manager
**Escenario**: Cada lunes por la mañana necesita saber qué pasó la semana anterior
**Input**: Archivos CSV exportados de sistema de tickets + mensajes de Slack
**Proceso**: Agente lee todos los inputs, analiza, genera reporte
**Output**: Email con reporte ejecutivo + archivo markdown guardado
**Tiempo esperado**: 2-3 minutos

### Caso de Uso 2: Análisis Ad-Hoc Después de Lanzamiento
**Usuario**: Product Owner
**Escenario**: Lanzaron nueva feature y quieren feedback inmediato
**Input**: Feedback de últimos 3 días en JSON
**Proceso**: Análisis rápido enfocado en la nueva feature
**Output**: Reporte focalizado con sentimiento y bugs críticos
**Tiempo esperado**: 1 minuto

### Caso de Uso 3: Identificación de Bug Crítico
**Usuario**: Sistema automático (cron job)
**Escenario**: Corre cada 6 horas para detectar bugs críticos
**Input**: Feedback en tiempo real
**Proceso**: Solo busca bugs críticos y problemas de acceso
**Output**: Alerta inmediata a Slack #tech-alerts si detecta patrón crítico
**Tiempo esperado**: 30 segundos

---

## 7. Manejo de Errores

### Errores Comunes y Soluciones
1. **Error**: Archivo CSV con formato incorrecto
   - **Causa**: Columnas faltantes o nombres diferentes
   - **Solución**: Registrar error en log, enviar email a admin, continuar con otros archivos

2. **Error**: API de Slack no responde
   - **Causa**: Rate limit o servicio caído
   - **Solución**: Reintentar 3 veces con backoff, si falla omitir Slack y notificar

3. **Error**: Texto en idioma no soportado
   - **Causa**: Feedback en idioma diferente a inglés/español
   - **Solución**: Detectar idioma, intentar traducir, o marcar como "requiere revisión manual"

### Escalación a Humano
¿Cuándo debe el agente pedir ayuda humana?
- Cuando detecta patrón crítico pero no está 100% seguro (ej. posible data breach)
- Cuando >30% del feedback está en idioma no soportado
- Cuando encuentra feedback contradictorio sobre el mismo tema

### Logs y Monitoreo
- [x] Registrar todas las ejecuciones
- [x] Registrar solo errores
- [x] Notificar al equipo en caso de falla
- [x] Dashboard de monitoreo (futuro)

---

## 8. Contexto y Memoria

### ¿Necesita mantener contexto entre ejecuciones?
- [x] Sí

Si sí, ¿qué debe recordar?
- Memoria 1: Temas ya reportados semana anterior (para detectar tendencias)
- Memoria 2: Clientes que han dado feedback (para contar únicos)
- Memoria 3: Features ya priorizadas (para no repetir)

### ¿Dónde se almacena el contexto?
- [x] JSON local
- [ ] Base de datos
- [ ] Cache en memoria
- [ ] Otro: [Especificar]

Archivo: `/data/feedback_context.json`

---

## 9. Criterios de Éxito

### Métricas de Desempeño
- **Precisión**: 90% de clasificaciones correctas (validado manualmente)
- **Velocidad**: < 3 minutos para analizar 100+ piezas de feedback
- **Cobertura**: 100% del feedback procesado sin pérdida

### Criterios de Aceptación
- [x] Criterio 1: Identifica correctamente top 3 temas más mencionados
- [x] Criterio 2: Detecta bugs críticos con 95% de precisión
- [x] Criterio 3: Genera reporte legible sin intervención humana
- [x] Criterio 4: Deduplica correctamente clientes (no cuenta 2 veces)

### Pruebas Necesarias
1. Test 1: Dataset de 50 feedbacks etiquetados manualmente
2. Test 2: Feedback con bugs críticos conocidos (debe detectarlos)
3. Test 3: Feedback duplicado (debe agrupar correctamente)

---

## 10. Configuración y Deployment

### Variables de Entorno
```env
ANTHROPIC_API_KEY=sk-ant-...
SLACK_BOT_TOKEN=xoxb-...
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=bot@answering.com
SMTP_PASSWORD=...
AGENTE_MODEL=claude-3-sonnet-20240229
AGENTE_TEMPERATURE=0.3
AGENTE_MAX_TOKENS=4000
```

### Cómo Ejecutarlo
```bash
# Manual
python agentes/feedback-analyzer.py --input data/feedback_week12.json --output reports/

# Automático (cron)
0 8 * * 1 python agentes/feedback-analyzer.py --auto --email
```

### Frecuencia de Ejecución
- [ ] Manual (on-demand)
- [ ] Cada hora
- [ ] Diario
- [x] Semanal (Lunes 8am)
- [x] Trigger por evento: Después de cada lanzamiento importante

### Dónde Corre
- [x] Local (desarrollo)
- [x] Servidor (producción con cron)
- [ ] Cloud (Lambda, Cloud Functions)
- [ ] Contenedor (Docker)

---

## 11. Ejemplos Completos

### Ejemplo 1: Ejecución Exitosa
**Input**:
```json
{
  "fuente": "tickets",
  "periodo": "2026-03-18 to 2026-03-25",
  "feedback": [
    {"id": 1, "cliente": "cliente1@example.com", "texto": "No puedo exportar reportes en PDF"},
    {"id": 2, "cliente": "cliente2@example.com", "texto": "Necesito exportar a PDF urgente"},
    {"id": 3, "cliente": "cliente3@example.com", "texto": "El dark mode sería genial"}
  ]
}
```

**Proceso interno del agente**:
```
1. Valida JSON ✓
2. Procesa 3 piezas de feedback
3. Identifica temas:
   - "Export PDF": 2 menciones, 2 clientes
   - "Dark mode": 1 mención, 1 cliente
4. Clasifica: 2 Feature Requests, 0 Bugs
5. Analiza sentimiento: Neutral/Constructivo
6. Genera reporte
```

**Output**:
```markdown
# Análisis de Feedback - Semana del 18-25 Marzo 2026

## Resumen Ejecutivo
- Total feedback procesado: 3
- Clientes únicos: 3
- Sentimiento general: Neutral (100%)

## Top Solicitudes
1. **Export a PDF** - 2 menciones, 2 clientes
   > "No puedo exportar reportes en PDF" - cliente1@example.com

## Recomendaciones
- Priorizar feature de export a PDF (alta demanda)
```

### Ejemplo 2: Manejo de Error
**Input**:
```json
{
  "fuente": "tickets",
  "feedback": []
}
```

**Output**:
```json
{
  "status": "warning",
  "mensaje": "No hay feedback para analizar en el periodo especificado",
  "recomendacion": "Verificar que las fuentes de datos estén funcionando"
}
```

---

## 12. Iteraciones Futuras

### Features Deseables (No MVP)
- [x] Feature 1: Detección automática de idioma y traducción
- [x] Feature 2: Dashboard interactivo con gráficos
- [x] Feature 3: Análisis de tendencias mes a mes
- [x] Feature 4: Integración con Jira para crear tickets automáticamente
- [x] Feature 5: Análisis de sentimiento más sofisticado (emociones específicas)

### Mejoras Potenciales
- Mejora 1: Machine learning para mejorar agrupación con el tiempo
- Mejora 2: Integración con sistema CRM para enriquecer datos de clientes
- Mejora 3: Comparación con competencia (feedback público)

---

## 13. Referencias y Recursos

### Documentación Relevante
- [Anthropic API Docs](https://docs.anthropic.com)
- [Slack API - Reading messages](https://api.slack.com/methods/conversations.history)
- [NLP para análisis de sentimiento](https://huggingface.co/tasks/sentiment-analysis)

### Agentes Similares
- Agente de análisis de reviews (App Store) - Similar pero para reviews públicas
- Sentiment analyzer - Podemos reutilizar lógica de clasificación

### Inspiración
- Zendesk Explore (reportes automáticos)
- Enterpret (plataforma de análisis de feedback)

---

## 14. Notas Adicionales

Este agente es crítico para el equipo de producto. La clave es que sea confiable y no pierda feedback importante. Mejor pecar de conservador (reportar más) que omitir bugs críticos.

Considerar privacidad: nunca exponer emails de clientes en reportes compartidos públicamente.

---

## 15. Checklist para Desarrollo

Para el equipo de desarrollo, antes de considerar el agente completo:

- [ ] Prompt principal definido y testeado
- [ ] Todas las herramientas integradas (Slack API, Email)
- [ ] Manejo de errores implementado
- [ ] Logs configurados
- [ ] Tests escritos y pasando (mínimo 3)
- [ ] Documentación actualizada
- [ ] Variables de entorno documentadas
- [ ] Ejemplo de uso incluido
- [ ] README del agente creado
- [ ] Registrado en CHANGELOG.md
