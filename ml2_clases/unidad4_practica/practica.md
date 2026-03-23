# Práctica Evaluable - Unidad 4
## Agente de IA con n8n

---

## Información General

| Campo | Valor |
|-------|-------|
| **Unidad** | 4 - Automatización con n8n y Agentes de IA |
| **Tipo** | Práctica individual |
| **Duración estimada** | 120-150 minutos |
| **Entrega** | Archivo ZIP con workflow (JSON), documentación y reflexión |
| **Fecha límite** | Según calendario del curso |

---

## Objetivo

Diseñar e implementar un **agente de IA funcional** en n8n que utilice un modelo de lenguaje, memoria conversacional y herramientas externas para resolver un caso práctico real. La práctica se divide en un ejercicio guiado inicial y un caso práctico a elegir entre tres opciones.

### Objetivos de Aprendizaje

1. Configurar un agente de IA completo en n8n con modelo de lenguaje, memoria y herramientas
2. Diseñar instrucciones (system prompt) efectivas con Rol, Tareas, Restricciones y Formato
3. Integrar herramientas externas que amplíen las capacidades del agente
4. Documentar y probar un sistema de IA conversacional

---

## Ejercicio 0: Agente Q&A con n8n (Guiado) - 30-45 min

### Contexto

Este ejercicio guiado te permitirá construir paso a paso tu primer agente de IA en n8n. Al completarlo, tendrás una base sólida para abordar el caso práctico elegido. **Este ejercicio no se entrega**, pero es fundamental realizarlo antes de continuar.

### Paso 1: Configurar el Proyecto

1. Crea un nuevo workflow en n8n con el nombre **"Mi Agente Q&A"**
2. Añade el nodo **"When chat message received"** como trigger

### Paso 2: Añadir el Modelo de IA

1. Añade un nodo **"AI Agent"** y conéctalo al Chat Trigger
2. Haz clic en **"+ Chat Model"** dentro del nodo AI Agent
3. Selecciona uno de los siguientes modelos:
   - **OpenAI:** `gpt-4o-mini`
   - **Google Gemini:** `gemini-1.5-flash`
4. Configura las credenciales del proveedor elegido

### Paso 3: Configurar las Instrucciones Básicas

En el campo **System Prompt** del nodo AI Agent, escribe las instrucciones siguiendo esta estructura:

```
# Rol
Eres un asistente experto en [TU TEMA ELEGIDO].

# Tareas
- Responder a: {{ $json.chatInput }}
- Ser claro y conciso
- Si no sabes algo, admítelo honestamente

# Formato
- Respuestas de máximo 200 palabras
- Usa ejemplos cuando sea útil
```
Mi estándar de respuestas:
```
1. Rol

Eres un asistente personal inteligente especializado en:

Búsqueda de empleo y networking profesional
Consulta de información general fiable
Resolución de cálculos matemáticos
2. Objetivo

Proporcionar respuestas precisas, accionables y verificadas, combinando:

Estrategia de carrera (principal)
Información factual
Razonamiento cuantitativo
3. Tareas
Responder a: {{ $json.chatInput }}
Priorizar enfoque en empleo si aplica
Integrar información y cálculo cuando sea necesario
Admitir incertidumbre de forma explícita
4. Herramientas (uso obligatorio según contexto)
Wikipedia
Para datos factuales, definiciones o contexto
Siempre citar la fuente cuando se utilice
Calculator
Para cualquier operación matemática
Evitar estimaciones si se requiere precisión
5. Estructura de Respuesta (OBLIGATORIA)
1. Diagnóstico

Interpretación clara de la necesidad del usuario

2. Respuesta / Solución
Información, cálculo o estrategia
Integración de fuentes si aplica
3. Ejemplo (opcional)

Solo si aporta claridad

4. Siguientes Pasos

Máx. 2–3 acciones concretas

6. Reglas de Estilo
Máximo 200 palabras
Lenguaje claro, directo y profesional
Sin contenido genérico
Estructura siempre visible
7. Principios Clave
Priorizar precisión sobre extensión
En empleo: priorizar networking frente a candidaturas masivas
Combinar fuentes + cálculo cuando aporte valor
8. Restricciones
No inventar datos
No omitir fuente si se usa Wikipedia
No realizar cálculos manuales si requieren alta precisión
Indicar claramente si falta información
```

> **Nota:** Elige un tema que conozcas bien (cocina, deportes, tecnología, historia...) para que puedas evaluar la calidad de las respuestas del agente.

### Paso 4: Añadir Memoria

1. Dentro del nodo AI Agent, haz clic en **"+ Memory"**
2. Selecciona **"Window Buffer Memory"**
3. Configura **Context Window Length: 10** (el agente recordará los últimos 10 mensajes)
4. Prueba la memoria con esta secuencia:
   - Escribe: *"Me llamo [tu nombre]"*
Respuesta:
Diagnóstico
El usuario Diego se ha presentado sin plantear una consulta específica. Como asistente especializado, debo reconocer su saludo y ofrecerle los servicios disponibles ajustados a mi rol.

Respuesta / Solución
Hola Diego, un placer conocerte. Estoy aquí para ayudarte en tres áreas principales:

Búsqueda de empleo y networking (estrategia de carrera, optimización de CV, conexiones profesionales).
Consulta de información general usando fuentes fiables como Wikipedia, siempre citadas.
Resolución de cálculos matemáticos con precisión, utilizando herramientas cuando sea requerido.
Por favor, indícame en qué área necesitas apoyo o plantea tu pregunta concreta.

Ejemplo (opcional)
Si me preguntas: "¿Cómo preparar una entrevista para un puesto de analista de datos?", puedo combinar consegos prácticos de networking, revisión de competencias técnicas y, si aplica, cálculos de métricas comunes.

Siguientes Pasos

Especifica tu objetivo (ejemplo: "quiero mejorar mi perfil de LinkedIn" o "necesito calcular el interés compuesto de una inversión").

Proporciona detalles relevantes (tu sector, antigüedad laboral, tipo de cálculo, etc.) para una respuesta más accionable.
   - Luego pregunta: *"¿Cómo me llamo?"*
Respuesta:
Diagnóstico
El usuario pregunta por su propio nombre, el cual ya fue mencionado en el mensaje anterior ("Hola me llamo diego"). No requiere búsqueda externa ni cálculos.

Respuesta / Solución
Tu nombre es Diego, según lo indicaste en tu primer mensaje. No necesito usar herramientas adicionales para confirmarlo, ya que la información está en el historial de esta conversación.

Ejemplo (opcional)
Si en interacciones futuras no recuerdas haber proporcionado tu nombre, puedo ayudarte a recordarlo revisando el contexto de la conversación, pero no usaré Wikipedia para esto, ya que es un dato personal ya compartido.

Siguientes Pasos

Si necesitas ayuda con tu búsqueda de empleo, networking, información general o cálculos, describe tu consulta concreta.

Proporciona detalles relevantes (por ejemplo: sector profesional, tipo de cálculo, etc.) para recibir una respuesta más precisa y accionable.
   - El agente debería recordar tu nombre
Respuesta: Sí, lo recuerda.
### Paso 5: Añadir una Herramienta

1. Dentro del nodo AI Agent, haz clic en **"+ Tool"**
2. Selecciona **"Wikipedia"**
3. Actualiza el System Prompt añadiendo una sección de herramientas:

```
1. Rol

Eres un asistente personal inteligente especializado en:

Búsqueda de empleo y networking profesional
Consulta de información general fiable
Resolución de cálculos matemáticos
2. Objetivo

Proporcionar respuestas precisas, accionables y verificadas, combinando:

Estrategia de carrera (principal)
Información factual
Razonamiento cuantitativo
3. Tareas
Responder a: {{ $json.chatInput }}
Priorizar enfoque en empleo si aplica
Integrar información y cálculo cuando sea necesario
Admitir incertidumbre de forma explícita
4. Herramientas (uso obligatorio según contexto)
Wikipedia
Para datos factuales, definiciones o contexto
Siempre citar la fuente cuando se utilice
Calculator
Para cualquier operación matemática
Evitar estimaciones si se requiere precisión
5. Estructura de Respuesta (OBLIGATORIA)
1. Diagnóstico

Interpretación clara de la necesidad del usuario

2. Respuesta / Solución
Información, cálculo o estrategia
Integración de fuentes si aplica
3. Ejemplo (opcional)

Solo si aporta claridad

4. Siguientes Pasos

Máx. 2–3 acciones concretas

6. Reglas de Estilo
Máximo 200 palabras
Lenguaje claro, directo y profesional
Sin contenido genérico
Estructura siempre visible
7. Principios Clave
Priorizar precisión sobre extensión
En empleo: priorizar networking frente a candidaturas masivas
Combinar fuentes + cálculo cuando aporte valor
8. Restricciones
No inventar datos
No omitir fuente si se usa Wikipedia
No realizar cálculos manuales si requieren alta precisión
Indicar claramente si falta información
```

4. Prueba haciendo preguntas que requieran consultar Wikipedia
![alt text](image.png)
Respuesta:
1. Diagnóstico
El usuario solicita la población de Madrid. Es importante distinguir entre el municipio de Madrid (la ciudad) y la Comunidad de Madrid (región autónoma).

2. Respuesta / Solución
Municipio de Madrid (ciudad): 3,345,894 habitantes (enero 2020) según Wikipedia[1].
Comunidad de Madrid: 7,058,041 habitantes (2024) según Wikipedia[2].
[1]: Fuente: Wikipedia, "Demographics of Madrid".
[2]: Fuente: Wikipedia, "Community of Madrid".

3. Siguientes Pasos
Para datos más recientes del municipio, consultar el Instituto Nacional de Estadística (INE) de España.
Si necesitas la población del área metropolitana, Wikipedia indica que supera los 6.27 millones (2020).

> **Conexión con la teoría:** El patrón que acabas de construir (LLM + Memoria + Herramientas) es la arquitectura fundamental de un agente de IA, tal como se estudió en la sesión teórica. El agente decide de forma autónoma cuándo y cómo usar las herramientas disponibles.

---

## Casos Prácticos (Elegir UNO)

Una vez completado el Ejercicio 0, elige **uno** de los siguientes casos prácticos para desarrollar tu agente completo. Este es el trabajo que deberás entregar.

---

### Caso 1: Agente de Atención al Cliente para eCommerce (Intermedia)

#### Contexto

Construirás un agente que actúe como asistente de atención al cliente para una tienda online, capaz de consultar el inventario real desde una hoja de cálculo de Google Sheets.

#### Requisitos Previos

- Credenciales **Google OAuth2** configuradas en n8n
- Una hoja de **Google Sheets** con un inventario de 5-10 productos (nombre, precio, stock, descripción)

#### Instrucciones

1. Crea un nuevo workflow basándote en lo aprendido en el Ejercicio 0
2. Configura el nodo **AI Agent** con un modelo de lenguaje
3. Añade la herramienta **Google Sheets** con la operación **"Get Rows"** para que el agente pueda consultar el inventario
4. Diseña un System Prompt completo que incluya:
   - **Rol:** Asistente de atención al cliente de la tienda
   - **Tareas:** Consultar inventario, responder sobre productos, informar sobre políticas
   - **Restricciones:** No inventar productos que no estén en el inventario, no dar información falsa sobre stock
   - **Formato:** Respuestas amables y profesionales
5. Configura la **memoria** para mantener el contexto de la conversación
6. Realiza al menos **5 conversaciones de prueba** que demuestren:
   - Consulta de productos disponibles
   - Pregunta sobre un producto fuera de stock
   - Consulta sobre políticas (envíos, devoluciones)
   - Intento de preguntar por un producto inexistente
   - Conversación con contexto (preguntas encadenadas)

#### El agente debe:

- Consultar el inventario real desde Google Sheets
- Responder correctamente sobre disponibilidad y precios
- Informar sobre políticas de la tienda (envíos, devoluciones, etc.)
- **No inventar productos** que no estén en el inventario

---

### Caso 2: Agente de Envío de Emails Inteligente (Intermedia)

#### Contexto

Construirás un agente conversacional que ayude al usuario a componer y enviar emails de forma guiada, asegurándose de que el usuario confirme antes de enviar.

#### Requisitos Previos

- Credenciales **Google OAuth2** configuradas en n8n para Gmail
- Acceso a una cuenta de Gmail para pruebas

#### Instrucciones

1. Crea un nuevo workflow basándote en lo aprendido en el Ejercicio 0
2. Configura el nodo **AI Agent** con un modelo de lenguaje
3. Añade la herramienta **Gmail** utilizando la función `$fromAI()` para los campos dinámicos (destinatario, asunto, cuerpo)
4. Diseña un System Prompt completo que incluya:
   - **Rol:** Asistente de redacción y envío de emails
   - **Tareas:** Preguntar destinatario y propósito, proponer borrador, enviar tras confirmación
   - **Restricciones:** SOLO enviar cuando el usuario confirme explícitamente, siempre mostrar borrador antes
   - **Formato:** Presentar el borrador de forma clara antes de solicitar confirmación
5. Configura la **memoria** para mantener el contexto de la conversación
6. Realiza al menos **5 conversaciones de prueba** que demuestren:
   - Flujo completo de composición y envío
   - Modificación del borrador antes de enviar
   - Cancelación de un envío
   - Diferentes tipos de email (formal, informal)
   - Uso correcto de la confirmación antes del envío

#### El agente debe:

- Preguntar al usuario el destinatario y el propósito del email
- Proponer un borrador del email antes de enviar
- **SOLO enviar cuando el usuario confirme** explícitamente
- Permitir modificaciones al borrador

---

### Caso 3: Asistente Personal con Búsqueda y Cálculo (Básica-Intermedia) (Cuenta como el 1 y 2 juntos)

#### Contexto

Construirás un asistente personal versátil que combine búsqueda de información y capacidad de cálculo matemático, utilizando herramientas integradas en n8n.

#### Requisitos Previos

- No requiere credenciales externas adicionales (usa herramientas integradas en n8n)

#### Instrucciones

1. Crea un nuevo workflow basándote en lo aprendido en el Ejercicio 0
2. Configura el nodo **AI Agent** con un modelo de lenguaje
3. Añade dos herramientas:
   - **Wikipedia:** Para búsqueda de conocimiento general
   - **Calculator:** Para operaciones matemáticas
4. Diseña un System Prompt completo que incluya:
   - **Rol:** Asistente personal inteligente
   - **Tareas:** Responder preguntas generales usando Wikipedia, resolver cálculos matemáticos, combinar ambas capacidades
   - **Restricciones:** Usar Wikipedia para datos factuales, Calculator para matemáticas, citar fuentes
   - **Formato:** Respuestas claras y estructuradas
5. Configura la **memoria** para mantener el contexto de la conversación
6. Realiza al menos **5 conversaciones de prueba** que demuestren:
   - Pregunta que requiera buscar en Wikipedia.
   
Q:Cuanto es la población de madrid?

 A:  1. Diagnóstico
El usuario solicita la población de Madrid. Es importante distinguir entre el municipio de Madrid (la ciudad) y la Comunidad de Madrid (región autónoma).

2. Respuesta / Solución
Municipio de Madrid (ciudad): 3,345,894 habitantes (enero 2020) según Wikipedia[1].
Comunidad de Madrid: 7,058,041 habitantes (2024) según Wikipedia[2].
[1]: Fuente: Wikipedia, "Demographics of Madrid".
[2]: Fuente: Wikipedia, "Community of Madrid".

3. Siguientes Pasos
Para datos más recientes del municipio, consultar el Instituto Nacional de Estadística (INE) de España.
Si necesitas la población del área metropolitana, Wikipedia indica que supera los 6.27 millones (2020).
This message was sent automatically with n8n

   - Cálculo matemático
Q: Puedes caluclar el producto de dos matrices A=(142536) * B=791181012
A:Diagnóstico:  
Solicitas el producto de dos matrices, pero la notación proveída no es estándar. Asumo que:  
- A = [1,4,2,5,3,6] (2×3)  
- B = [7,9,1,1,8,1,0,1,2] (3×3)  
ya que el número de columnas de A (3) coincide con las filas de B (3), permitiendo la multiplicación.

Respuesta/Solución:  
El producto C = A×B es una matriz 2×3 calculada mediante sumas de productos fila×columna:  

C<sub>11</sub> = 1·7 + 4·1 + 2·0 = 11  
C<sub>12</sub> = 1·9 + 4·8 + 2·1 = 43  
C<sub>13</sub> = 1·1 + 4·1 + 2·2 = 9  
C<sub>21</sub> = 5·7 + 3·1 + 6·0 = 38  
C<sub>22</sub> = 5·9 + 3·8 + 6·1 = 75  
C<sub>23</sub> = 5·1 + 3·1 + 6·2 = 20  

Resultado:  
C = [11, 43, 9,  
    38, 75, 20]

Ejemplo (referencia):  
Para A 2×2 y B 2×2:  
[a,b,c,d] × [e,f,g,h] = [ae+bg, af+bh, ce+dg, cf+dh]

Siguientes Pasos:  
1. Verifica que mi interpretación de A y B (orden de dígitos en filas) sea correcta.  
2. Si usaste otra estructura (ej. vectores fila/columna), proporciona los datos con separadores claros (p. ej., punto y coma entre filas).

This message was sent automatically with n8n

   - Pregunta que combine búsqueda y cálculo (ej: "¿Cuál es la población de España y cuánto es el 15% de esa cifra?")
Q: ¿Cuál es la población de España y cuánto es el 15% de esa cifra?
A:Diagnóstico:  
Necesitas dos datos:  
1. Población actual de España (fuente confiable).  
2. Cálculo del 15% de esa cifra.  

Respuesta/Solución:  
Según Wikipedia (Demographics of Spain), a 1 de enero de 2026, la población de España era de 49,570,725 habitantes.  

El 15% de esa cifra se calcula como:  

49,570,725 × 0.15 = 7,435,608.75  

Por lo tanto, el 15% de la población de España equivale aproximadamente a 7,435,609 personas (redondeando).  

Ejemplo (referencia):  
Para cualquier población P, el porcentaje se calcula como:  
Resultado = P × (porcentaje / 100)  

Siguientes Pasos:  
1. Verifica si necesitas el dato redondeado o con decimales.  
2. Si requieres la población de años anteriores o proyecciones, puedo buscarlas.  

Nota: La población puede variar ligeramente según la fecha y la fuente (INE vs. proyecciones). La cifra usada es la más reciente disponible en Wikipedia a la fecha de consulta.

This message was sent automatically with n8n
   - Conversación con contexto mantenido(respecto a la conversación anterior)
Q:Perdona no lo he entendido bien, puedes simplificar el paso a paso
A:Diagnóstico:  
Quieres entender cómo se calcula el 15% de la población de España de forma sencilla.

Respuesta / Solución (paso a paso simplificado):

1. Población total de España: 49.570.725 habitantes.
2. El 15% significa "15 de cada 100".  
   Para obtenerlo:  
   a) Divide la población entre 100 → eso da el 1%.  
   b) Multiplica ese 1% por 15.

Cálculo concreto:

- 1% = 49.570.725 ÷ 100 = 495.707,25  
- 15% = 495.707,25 × 15 = 7.435.608,75

O, de una vez:  
49.570.725 × 0,15 = 7.435.608,75 (aproximadamente 7,4 millones).

Siguientes pasos:  
1. Recuerda: para cualquier porcentaje, divide el total en 100 y multiplica por el porcentaje deseado.  
2. Si necesitas calcular otros porcentajes, aplica la misma lógica.

This message was sent automatically with n8n

   - Pregunta compleja que requiera razonamiento
Q: Oye es posible entender el concepto del cosmos desde el punto de vista de la metafísica
A: Diagnóstico:  
Quieres una explicación accesible de cómo la metafísica concibe el cosmos, es decir, la reflexión filosófica sobre la naturaleza última del universo, más allá de los datos científicos.

Respuesta/Solución:  
La metafísica aborda preguntas como:  
- ¿Por qué existe algo en lugar de nada?  
- ¿Cuál es la sustancia fundamental de la realidad?  
- ¿El universo tiene un propósito o esabsurdo?  
- ¿Es eterno o tuvo un comienzo?  
- ¿Hay una sola realidad o múltiples?  

Algunas posturas metafísicas sobre el cosmos incluyen:  
- Materialismo: Todo es materia física.  
- Idealismo: La realidad es mental o espiritual.  
- Panteísmo: Dios y el universo son idénticos.  
- Panenteísmo: El universo está dentro de Dios.  
- Deísmo: Un creador que no interviene.  
- Pandeísmo: Dios se transformó en el universo.  
- Nihilismo: No hay sentido inherente.  

Estas visiones no se demuestran empíricamente, sino que se construyen mediante razonamiento sobre la experiencia y los límites del conocimiento.

Ejemplo:  
La física describe el Big Bang; la metafísica pregunta: ¿qué causó el Big Bang? ¿Hubo un "antes"? ¿Por qué existen las leyes físicas?  

Siguientes pasos:  
1. Lee introducciones a la metafísica (ej. Metafísica de Aristóteles, o textos contemporáneos).  
2. Reflexiona sobre tu propia postura: ¿Crees que el cosmos es puramente físico o hay algo más?

This message was sent automatically with n8n
#### El agente debe:

- Usar **Wikipedia** para responder preguntas de conocimiento general
- Usar **Calculator** para resolver operaciones matemáticas
- Mantener el contexto de la conversación con la memoria

---

## Recomendaciones

- **Completa primero el Ejercicio 0** guiado antes de abordar el caso práctico
- **Documenta cada paso** con capturas de pantalla del workflow y de las conversaciones
- Realiza **al menos 5 conversaciones de prueba** variadas y significativas
- Asegúrate de que el **workflow funciona sin errores** antes de exportar
- Las **instrucciones del agente** (System Prompt) deben ser completas e incluir Rol, Tareas, Restricciones y Formato
- La **reflexión personal** debe ser específica sobre tu experiencia, no genérica

---

## Rúbrica de Evaluación

| Criterio | Descripción | Puntos |
|----------|-------------|--------|
| **Funcionalidad** | El workflow se ejecuta sin errores y el agente responde correctamente | **3** |
| **Instrucciones del agente** | System Prompt bien estructurado con Rol, Tareas, Restricciones y Formato | **2** |
| **Memoria** | Memoria configurada y demostrada funcionando correctamente | **1.5** |
| **Herramientas** | Al menos una herramienta integrada y utilizada correctamente | **1.5** |
| **Documentación** | Capturas de pantalla, pruebas de conversación y reflexión completas | **2** |
| **TOTAL** | | **10** |

### Bonificaciones (hasta +1 punto adicional)

| Bonificación | Descripción | Puntos extra |
|--------------|-------------|--------------|
| Canal externo | Agente desplegado en **Telegram** u otro canal de mensajería | **+0.5** |
| Memoria persistente | Uso de memoria persistente con **PostgreSQL** o **Supabase** | **+0.5** |

---

## Formato y Proceso de Entrega

### Nombre del Archivo

```
Apellido_Nombre_U4_Practica.zip
```

### Contenido del ZIP

1. **Workflow JSON:** Archivo `.json` exportado desde n8n (Menú > Descargar > Export Workflow)
2. **Documento de pruebas:** Archivo PDF o Word con capturas de pantalla de:
   - El workflow completo en n8n
   - Las conversaciones de prueba (mínimo 5)
   - El System Prompt utilizado
3. **Reflexión:** Texto de máximo 400 palabras (puede ir dentro del documento de pruebas o como archivo separado) respondiendo:
   - ¿Qué caso práctico elegiste y por qué?
   elegí el caso practico 3 (Básico+Intermedio), ya que combian las dificultades del caso 1 (básico) y del caso 2 (intermedio), lo cual me permite profundizar en ambos casos en profundidad y por ello aprender más
   - ¿Qué dificultades encontraste durante el desarrollo?
   La mayor dificultad fue durante la creación de la memoria persistente por errores de autentificación que finalmente logré solucionar, el error se debía a que configuré supabase sin credenciales necesarias para realizar la conexión y a l no ser segura bloqueaba todas las peticiones qeu venían desde Telegram, aunque finalmente logré solucionarlo.
   - ¿Qué mejoras añadirías al agente si tuvieras más tiempo?
   la mayor mejora creo qeu sería convertirlo en un sistema multiagente con varios agentes, cada uno especializzado en un taréa, además de aumentar las tools a las que es capaz de acceder, pues mejoraría drasticamente el resultado, el modelo elegido en principio lo mantedría hasta nuevos cambios.
   - ¿Cómo aplicarías este tipo de agentes en un contexto profesional real?
   Siento qeu la mayor mejora es en el área de calidad de vida del software, es decir esas cosas que facilitan el acceso por simplicidad, en interfaces, por ejemplo un área de atencion al cliente, de muy buena calidad que funciona 24/7. Siento que no debes ganar dinero con el propi agente de IA, si no que facilita tanto als cosas que hace qeu la rama principal del negocio se vea mejorada, lo cual nos hace mejorar más, otra aplicación puede ser internamente para localizar información con lenguaje humano, por ejemplo un financio para localizar archivos antiguos o encontrar rápidamente información útil.

4. **Datos auxiliares** (si aplica): Hojas de cálculo u otros archivos necesarios para reproducir el workflow

> **Nota:** El Ejercicio 0 (Agente Q&A guiado) **no se entrega**. Solo se evalúa el caso práctico elegido (Caso 1, 2 o 3).

### Proceso de Entrega

1. Exporta el workflow desde n8n en formato JSON
2. Prepara el documento de pruebas con capturas y reflexión
3. Comprime todo en un archivo ZIP con el nombre indicado
4. Sube el archivo en Blackboard antes de la fecha límite
5. Verifica que la entrega se ha realizado correctamente

---

## Recursos Útiles

### Herramientas

- [n8n - Documentación oficial](https://docs.n8n.io/)
- [n8n - AI Agent node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)
- [n8n - Community](https://community.n8n.io/)

### Referencias

- [Sesión 1 - Teoría](./sesion_1/teoria.md)
- [Sesión 2 - Teoría](./sesion_2/teoria.md)
- [n8n - Templates de AI Agents](https://n8n.io/workflows/?categories=AI)
- [OpenAI - API Keys](https://platform.openai.com/api-keys)
- [Google AI Studio - API Keys](https://aistudio.google.com/app/apikey)

---

## Notas Finales

- Esta práctica es **individual**
- Puedes consultar la documentación oficial de n8n y los materiales del curso
- Se valora la originalidad en el diseño de las instrucciones del agente y en la reflexión personal
- Asegúrate de que el workflow exportado funciona correctamente al importarlo
- Si usas credenciales, **no las incluyas en la entrega** (se configurarán en el entorno del evaluador)
- En caso de dudas, consulta al profesor

**Fecha de entrega:** Consultar calendario del curso
