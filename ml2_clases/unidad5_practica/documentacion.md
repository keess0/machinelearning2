# Documentación del Proyecto — Asistente RAG TechCorp

## 1. Arquitectura del Sistema

El sistema implementa el patrón RAG completo en dos fases diferenciadas: ingesta y consulta.

### Flujo de Ingesta

```
Documentos .txt → DirectoryLoader → RecursiveCharacterTextSplitter
                                             ↓
                                    OpenAIEmbeddings (text-embedding-ada-002)
                                             ↓
                                    ChromaDB (persisted en ./chroma_db)
```

### Flujo de Consulta

```
Pregunta del usuario
        ↓
OpenAIEmbeddings → vector de consulta
        ↓
ChromaDB similarity search (k=3) → 3 chunks más relevantes
        ↓
Prompt + Contexto recuperado
        ↓
ChatOpenAI (gpt-4o-mini, temperature=0.3) → Respuesta
```

Los dos archivos principales son `ingesta.py` (fase offline, se ejecuta una sola vez) y `asistente.py` (fase online, bucle interactivo por CLI). Para el bonus se añade `interfaz_web.py` con una interfaz Gradio accesible desde el navegador.

---

## 2. Decisiones Técnicas

**Opción elegida: Opción B — LangChain + ChromaDB (Python)**

Elegí la opción Python porque me resulta más fácil controlar exactamente lo que está pasando en cada paso. Con n8n tienes menos visibilidad sobre cómo se hacen las cosas internamente, y creo que para entender RAG bien vale la pena ver el código. Además, ChromaDB funciona completamente en local, lo que significa que no necesito crear cuentas en servicios externos como Pinecone.

**Tamaño de chunk: 300 caracteres con overlap de 30**

Empecé con 300 porque la práctica lo sugería como valor inicial. Después de ver que los documentos tienen secciones numeradas relativamente cortas (cada punto tiene unos 3-5 párrafos breves), 300 me pareció un buen equilibrio. Con 500 los chunks eran demasiado largos y mezclaban conceptos distintos. Con 200 algunos chunks quedaban cortados en medio de una instrucción, perdiendo contexto.

**Número de documentos recuperados: k=3**

Con k=3 el sistema trae suficiente contexto para responder la mayoría de preguntas. En la prueba de la pregunta sobre el procedimiento de reporte de incidencias, los 3 chunks cubrían exactamente los pasos a, b, c, d, e del proceso. Probé con k=2 y a veces faltaba algún paso. Con k=5 el contexto era más largo de lo necesario y el modelo tendía a repetirse.

**Modelo y temperatura: gpt-4o-mini, temperature=0.3**

`gpt-4o-mini` es suficientemente capaz para este tipo de recuperación de información factual y es bastante más barato que gpt-4o. La temperatura de 0.3 hace que las respuestas sean bastante consistentes sin ser completamente rígidas. Para una consulta de RRHH prefiero respuestas predecibles a respuestas creativas.

---

## 3. Ejemplos de Funcionamiento

### Consulta 1: ¿Cuántos días de vacaciones tengo al año?

**Documentos recuperados:**
- `documentos/politicas_rrhh.txt` — sección "2. VACACIONES Y PERMISOS" (chunk 1)
- `documentos/politicas_rrhh.txt` — sección "2. VACACIONES Y PERMISOS" (chunk 2)
- `documentos/politicas_rrhh.txt` — sección "1. HORARIO LABORAL"

**Respuesta del sistema:**
```
Asistente: Según la política de RRHH de TechCorp (documento: politicas_rrhh.txt),
cada empleado dispone de 23 días laborables de vacaciones al año. Ten en cuenta que:

- Las vacaciones deben solicitarse con al menos 15 días de antelación a través
  del portal del empleado.
- No se pueden acumular más de 5 días de vacaciones de un año para otro.
- Los permisos por asuntos propios son adicionales: máximo 3 días al año,
  comunicados con 48 horas de antelación.
```

**Evaluación:** Correcta y completa. Cita la fuente. Incluye matices relevantes sobre la política sin inventar información adicional.

---

### Consulta 2: ¿Cuál es el procedimiento para reportar una incidencia técnica?

**Documentos recuperados:**
- `documentos/procedimiento_soporte.txt` — sección "2. PROCESO DE REPORTE"
- `documentos/procedimiento_soporte.txt` — sección "1. CLASIFICACIÓN DE INCIDENCIAS"
- `documentos/procedimiento_soporte.txt` — sección "3. ESCALADO DE INCIDENCIAS"

**Respuesta del sistema:**
```
Asistente: Para reportar una incidencia técnica en TechCorp, sigue estos pasos
(procedimiento_soporte.txt, sección 2):

a) Accede al portal de soporte: soporte.techcorp.internal
b) Selecciona la categoría correspondiente: Hardware, Software, Red o Accesos
c) Describe el problema con el máximo detalle posible
d) Adjunta capturas de pantalla si son relevantes
e) Indica la urgencia y el impacto en tu trabajo

Una vez enviado, el sistema asignará automáticamente un número de ticket y
un técnico responsable.

Si tienes dudas sobre la prioridad de tu incidencia, existen tres niveles:
CRÍTICA (P1), ALTA (P2) y NORMAL (P3).
```

**Evaluación:** Correcta y muy completa. El sistema recuperó exactamente el chunk con los pasos y añadió contexto útil sobre los niveles de prioridad.

---

### Consulta 3: ¿Puedo trabajar desde casa todos los días de la semana?

**Documentos recuperados:**
- `documentos/politicas_rrhh.txt` — sección "3. TELETRABAJO"
- `documentos/politicas_rrhh.txt` — sección "1. HORARIO LABORAL"
- `documentos/politicas_rrhh.txt` — sección "3. TELETRABAJO" (chunk solapado)

**Respuesta del sistema:**
```
Asistente: No, no es posible trabajar desde casa todos los días de la semana.
Según la política de teletrabajo de TechCorp (politicas_rrhh.txt, sección 3):

- El máximo permitido es 2 días semanales de trabajo remoto.
- Las reuniones de equipo presenciales son obligatorias los martes y jueves.
- Para solicitar teletrabajo adicional más allá de los 2 días, se requiere
  aprobación del director de área.

Además, en todos los días de teletrabajo es obligatorio estar disponible
en horario laboral y utilizar la VPN corporativa.
```

**Evaluación:** Correcta. El sistema interpretó correctamente el matiz de la pregunta (implica un posible malentendido) y respondió con la restricción exacta.

---

### Consulta 4: ¿Cuál es el menú del comedor de la empresa?

**Documentos recuperados:**
- `documentos/politicas_rrhh.txt` — sección "1. HORARIO LABORAL"
- `documentos/politicas_rrhh.txt` — sección "6. CÓDIGO DE VESTIMENTA"
- `documentos/procedimiento_soporte.txt` — sección "4. MANTENIMIENTO PROGRAMADO"

**Respuesta del sistema:**
```
Asistente: No dispongo de información sobre ese tema en la documentación
de la empresa. Te recomiendo contactar con el departamento correspondiente.
```

**Evaluación:** Correcta para el caso negativo. El sistema no inventó nada. Recuperó chunks temáticamente alejados (lo más parecido que encontró fue el horario laboral y el comedor no aparece), pero reconoció que ninguno de ellos respondía la pregunta y activó el fallback definido en el prompt.

---

### Consulta 5: ¿Cada cuánto tiempo debo cambiar mi contraseña?

**Documentos recuperados:**
- `documentos/procedimiento_soporte.txt` — sección "5. POLÍTICA DE CONTRASEÑAS"
- `documentos/procedimiento_soporte.txt` — sección "5. POLÍTICA DE CONTRASEÑAS" (chunk solapado)
- `documentos/procedimiento_soporte.txt` — sección "6. SOFTWARE AUTORIZADO"

**Respuesta del sistema:**
```
Asistente: Según la política de contraseñas de TechCorp (procedimiento_soporte.txt,
sección 5), debes cambiar tu contraseña obligatoriamente cada 90 días.

Además, recuerda que:
- No puedes reutilizar ninguna de tus últimas 5 contraseñas.
- La contraseña debe tener al menos 12 caracteres, con mayúsculas, minúsculas,
  números y caracteres especiales.
- Tras 5 intentos fallidos, la cuenta se bloquea automáticamente. Para desbloquearla
  debes contactar con soporte técnico con identificación válida.
```

**Evaluación:** Correcta y completa. El sistema recuperó el chunk exacto de la política de contraseñas y añadió contexto complementario relevante.

---

## 4. Mejoras Propuestas

**1. Ampliar la base de documentos**

Actualmente el sistema solo tiene dos documentos. En una empresa real habría decenas: manual del empleado, procedimientos de cada departamento, FAQs de IT, políticas de seguridad, etc. Añadir más documentos mejoraría mucho la cobertura. También convendría añadir soporte para PDF y Word, no solo .txt.

**2. Implementar re-ranking de los documentos recuperados**

En algunos casos el retriever recupera chunks relevantes pero no siempre en el orden más útil. Añadir un paso de re-ranking (por ejemplo con un modelo cross-encoder o usando Cohere Rerank) mejoraría la calidad del contexto que llega al LLM. Creo que esto marcaría bastante diferencia cuando los documentos son más largos y heterogéneos.

**3. Añadir historial de conversación persistente**

El asistente actual no recuerda conversaciones anteriores. Cada sesión empieza desde cero. Para un uso real en empresa convendría guardar el historial en base de datos (por ejemplo SQLite) y permitir al usuario retomar conversaciones anteriores. Esto también permitiría al sistema aprender qué preguntas se hacen más y optimizar los documentos de respuesta.

---