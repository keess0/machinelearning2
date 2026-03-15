# Ejercicios Prácticos Tema 3 - Unidad 2, Sesión 1
## Fundamentos de Prompt Engineering

---

## Ejercicio 1: Anatomía de un Prompt

### Metadata
- **Duración estimada**: 20 minutos
- **Tipo**: Análisis
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de teoría sobre componentes del prompt

### Contexto
Antes de crear buenos prompts, es importante reconocer los componentes en prompts existentes.

### Objetivo de Aprendizaje
- Identificar los componentes de un prompt (rol, contexto, tarea, formato, restricciones)
- Evaluar la completitud de un prompt

### Enunciado
Analiza los siguientes prompts e identifica sus componentes. Indica qué componentes faltan y como los mejorarías.

### Prompt A
```
Eres un experto en marketing digital especializado en startups tecnológicas.

Contexto: Nuestra startup vende software de gestión de proyectos para equipos remotos.
Acabamos de lanzar una nueva funcionalidad de videoconferencias integradas.

Tarea: Escribe 3 posts para LinkedIn anunciando esta funcionalidad.

Formato:
- Cada post debe tener entre 100-150 palabras
- Incluir un emoji relevante al inicio
- Terminar con un call-to-action

No menciones competidores ni uses jerga demasiado técnica.
```

### Prompt B
```
Dame ideas para mejorar mi aplicación
```

### Prompt C
```
Traduce este texto al inglés y hazlo más formal:

"""
Hola! Queria saber si podemos quedar mañana para hablar del proyecto.
Avisame cuando puedas.
"""
```

### Tabla de Análisis

Completa la siguiente tabla para cada prompt:

| Componente | Prompt A | Prompt B | Prompt C |
|------------|----------|----------|----------|
| Rol | Si, experto en marketing digital para startups | No especificado | No especificado (indirectamente traductor profesional) |
| Contexto | Si, describe startup y lanzamiento de nueva funcion | No hay contexto | Parcial, solo da el texto a transformar |
| Tarea | Si, escribir 3 posts de LinkedIn | Si, pero muy vaga | Si, traducir al ingles y formalizar |
| Formato | Si, longitud, emoji inicial y cierre con CTA | No especificado | No especificado de forma explicita |
| Restricciones | Si, no mencionar comepetidores ni jerga tecnica | No hay | Parcial, idioma ingles y tono mas formal |
| Ejemplos | No incluye ejemplos de salida | No incluye | Incluye texto de entrada, pero no ejemplo de salida |
| **Evaluación (1-10)** | 9/10 | 2/10 | 6/10 |

### Preguntas de Reflexión
1. ¿Cuál de los tres prompts producirá mejores resultados? ¿Por qué?

En mi experiencia el Prompt A, ya que tener rol, contexto, tarea, formato y restricciones, reduce bastante la ambiguedad y mejora resultados.

2. ¿Qué añadirias al Prompt B para hacerlo efectivo?

Yo añadiria primero contexto de la aplicacion, audiencia y objetivo. Tambien pediria formato concreto (por ejemplo tabla con impacto y esfuerzo) y pondria restricciones como numero de ideas y enfoque tecnico o negocio.

3. ¿El Prompt C necesita rol? ¿Por qué si o por qué no?

No es obligatorio, porque la tarea es simple y puede funcionar sin rol. Aun asi, creo que un rol como "traductor profesional" mejoraria consistencia de tono y registro.

---

## Ejercicio 2: Zero-shot vs Few-shot

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Experimentación
- **Modalidad**: Individual
- **Dificultad**: Intermedia
- **Prerequisitos**: Acceso a ChatGPT, Claude o Gemini

### Contexto
Comparar el rendimiento de diferentes técnicas de prompting en una tarea de clasificación.

### Objetivo de Aprendizaje
- Experimentar con zero-shot y few-shot prompting
- Comparar resultados y entender cuándo usar cada técnica

### Enunciado
Vas a clasificar sentimientos de reseñas de productos usando tres enfoques diferentes.

### Parte A: Zero-shot (10 min)

Usa el siguiente prompt con 5 reseñas de prueba:

```
Clasifica el sentimiento de la siguiente reseña como: Positivo, Negativo o Neutro.
```

```
Respuestas individuales:

Reseña: "Excelente producto, superó mis expectativas. Lo recomiendo totalmente."

Sentimiento: Positivo

Reseña: "No funciona como esperaba. Devolución solicitada."

Sentimiento: Negativo

Reseña: "Esta bien para el precio. Hace lo que promete, nada más."

Sentimiento:Neutro


Reseña: "Llegó rápido pero la caja estaba dañada. El producto funciona correctamente."

Sentimiento: Neutro

Reseña: "HORRIBLE. Peor compra de mi vida. NO COMPREN."

Sentimiento: Negativo
```

**Reseñas de prueba:**
1. "Excelente producto, superó mis expectativas. Lo recomiendo totalmente."
2. "No funciona como esperaba. Devolución solicitada."
3. "Esta bien para el precio. Hace lo que promete, nada más."
4. "Llegó rápido pero la caja estaba dañada. El producto funciona correctamente."
5. "HORRIBLE. Peor compra de mi vida. NO COMPREN."

### Parte B: Few-shot (15 min)

Crea un prompt few-shot con 3 ejemplos (uno por categoría) y pruebalo con las mismas reseñas:

```
Clasifica el sentimiento de reseñas de productos en una de estas tres categorías:
Positivo, Negativo o Neutro.

Ejemplos:

Reseña: "Excelente calidad, funciona perfectamente y llegó antes de lo esperado."
Sentimiento: Positivo

Reseña: "Muy mala compra, el producto dejó de funcionar al segundo día."
Sentimiento: Negativo

Reseña: "Cumple su función, aunque no tiene nada especial."
Sentimiento: Neutro


Ahora clasifica las siguientes reseñas:

Reseña: "Excelente producto, superó mis expectativas. Lo recomiendo totalmente."
Sentimiento:

Reseña: "No funciona como esperaba. Devolución solicitada."
Sentimiento:

Reseña: "Esta bien para el precio. Hace lo que promete, nada más."
Sentimiento:

Reseña: "Llegó rápido pero la caja estaba dañada. El producto funciona correctamente."
Sentimiento:

Reseña: "HORRIBLE. Peor compra de mi vida. NO COMPREN."
Sentimiento:
```

```
Clasifica el sentimiento de reseñas de productos.

Ejemplos:
Reseña: "Excelente calidad, funciona perfectamente y llegó antes de lo esperado."
Sentimiento: Positivo

Reseña: "Muy mala compra, el producto dejó de funcionar al segundo día."
Sentimiento: Negativo

Reseña: "Cumple su función, aunque no tiene nada especial."
Sentimiento: Neutro

Ahora clasifica:
Reseña: "Excelente producto, superó mis expectativas. Lo recomiendo totalmente."
Sentimiento:
```

### Parte C: Comparación (5 min)

Completa la tabla:
NOTA: HE usado ChatGPT con un modelo muy ligero para aprenciar diferencias, modelos actuales no muestran tanta diferencia
| Reseña | Zero-shot | Few-shot | ¿Coinciden? |
|--------|-----------|----------|-------------|
| 1 | Positivo | Positivo | Si |
| 2 | Negativo | Negativo | Si |
| 3 | Neutro | Neutro | Si |
| 4 | Positivo | Neutro | No |
| 5 | Negativo | Negativo | Si |

### Preguntas
1. ¿Hubo diferencias en los resultados? ¿Cuáles?

Si, en mi prueba la diferencia estuvo en la reseña 4. En zero-shot salio Positivo por la frase "funciona correctamente", pero con few-shot quedo Neutro por mezcla de señal positiva y negativa.

2. ¿La reseña 4 fue difícil de clasificar? ¿Por qué?

Si, fue la mas ambigua. Tiene un problema logístico (caja dañada) y a la vez una valoracion funcional positiva del producto.

3. ¿Qué técnica usarias en producción? ¿Por qué?

Usaria few-shot para produccion porque da mas consistencia en casos frontera. Zero-shot me parece util para prototipar rapido, pero few-shot reduce variacion entre ejecuciones.

---

## Ejercicio 3: Desarrollo Iterativo de Prompts

### Metadata
- **Duración estimada**: 35 minutos
- **Tipo**: Programación/Iteración
- **Modalidad**: Parejas
- **Dificultad**: Intermedia
- **Prerequisitos**: Acceso a un LLM

### Contexto
El desarrollo iterativo es la clave del Prompt Engineering profesional. Vamos a practicar el ciclo completo.

### Objetivo de Aprendizaje
- Aplicar el proceso iterativo de mejora de prompts
- Documentar cambios y su impacto

### Enunciado
Desarrolla un prompt para generar descripciones de productos para e-commerce.

### Escenario
Trabajas en una tienda online de electrónica. Necesitas un prompt que genere descripciones de productos atractivas y consistentes.

**Producto de prueba:**
```
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Características:
- Cancelación de ruido activa
- 30 horas de bateria (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamaños de almohadillas
```

### Iteración 1: Prompt Básico

```
Escribe una descripción para este producto:
[datos del producto]
```

- Prueba el prompt y pega la respuesta
- ¿Qué problemas identificas?

Respuesta obtenida:

"Los EchoBuds Pro X3 son unos auriculares inalambricos con gran calidad de sonido, cancelacion de ruido y buena bateria. Son ideales para escuchar musica y hacer llamadas en cualquier lugar. Tienen Bluetooth 5.3 y resistencia al agua IPX5."

Problemas identificados:
- Es demasiado generica y no diferencia bien el producto.
- No tiene estructura clara para e-commerce.
- No conecta caracteristicas con beneficios concretos para el usuario.

### Iteración 2: Añadir Estructura

Mejora el prompt añadiendo:
- Formato de salida específico
- Longitud deseada

Documenta:
- Tu nuevo prompt
- La respuesta obtenida
- ¿Qué mejoro?

Tu nuevo prompt:

```
Actua como redactor de fichas de producto para e-commerce.

Escribe una descripcion de 120 a 140 palabras del siguiente producto:
[datos del producto]

Formato:
1. Titular corto (maximo 10 palabras)
2. Parrafo principal
3. Lista de 4 beneficios en bullet points
```

Respuesta obtenida:

"EchoBuds Pro X3: Sonido premium sin cables.\nLos EchoBuds Pro X3 ofrecen una experiencia de audio mas inmersiva gracias a su cancelacion de ruido activa y conectividad Bluetooth 5.3. Con hasta 30 horas de bateria total junto al estuche, estan pensados para acompanarte durante todo el dia.\n- Reduce el ruido del entorno para mayor concentracion.\n- Aguanta entrenamientos y lluvia ligera con IPX5.\n- Ajuste comodo con 3 tamanos de almohadillas.\n- Conexion estable y rapida con dispositivos modernos."

¿Qué mejoro?

Mejoro bastante la estructura y la legibilidad. Tambien aparecio mas enfoque en beneficios reales, no solo en listar specs.

### Iteración 3: Añadir Contexto y Tono

Mejora añadiendo:
- Audiencia objetivo
- Tono de la marca
- Elementos que debe incluir (beneficios, no solo características)

Prompt propuesto:

```
Eres copywriter de una tienda online de electronica orientada a profesionales jovenes que trabajan en remoto.

Producto:
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Caracteristicas:
- Cancelacion de ruido activa
- 30 horas de bateria (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamanos de almohadillas

Tarea:
Genera una descripcion comercial de 130 a 160 palabras.

Formato:
- 1 titular
- 1 parrafo principal
- 4 bullets de beneficios para teletrabajo, movilidad y comodidad

Tono:
Profesional cercano, claro y confiable.
```

Respuesta obtenida:

"EchoBuds Pro X3: productividad y sonido sin interrupciones.\nSi trabajas en remoto y necesitas concentracion real, los EchoBuds Pro X3 te ayudan a mantener el foco gracias a su cancelacion de ruido activa. Con 30 horas de autonomia total, puedes pasar de reuniones a musica sin estar pendiente del cargador. Su diseno IPX5 resiste salpicaduras y entrenamientos suaves, y las almohadillas en tres tallas mejoran el ajuste durante horas.\n- Menos distracciones en llamadas y trabajo profundo.\n- Bateria para toda la jornada laboral y desplazamientos.\n- Ajuste comodo para uso prolongado.\n- Conexion Bluetooth 5.3 rapida y estable."

¿Qué mejoro?

Aqui mejoro el encaje con audiencia y contexto de uso. Ya no suena como texto generico, sino como mensaje pensado para un perfil concreto.

### Iteración 4: Refinamiento Final

Ajusta para:
- Incluir call-to-action
- Añadir restricciones (evitar ciertas palabras, longitud exacta)
- Optimizar para SEO (si aplica)

Prompt final refinado:

```
Eres copywriter senior de e-commerce de electronica.

Objetivo: escribir una ficha de producto optimizada para conversion y SEO.

Producto:
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Caracteristicas:
- Cancelacion de ruido activa
- 30 horas de bateria (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamanos de almohadillas

Audiencia: profesionales y estudiantes que necesitan concentracion, movilidad y buena calidad de audio.

Instrucciones de salida:
- Longitud total: entre 145 y 155 palabras
- Incluir la frase clave: "auriculares inalambricos con cancelacion de ruido"
- Estructura: titulo, parrafo principal, 4 bullets y cierre con CTA
- No usar superlativos absolutos (como "el mejor del mundo")
- No inventar datos no incluidos en la ficha
```

Respuesta obtenida:

"EchoBuds Pro X3: enfocate donde estes\nLos EchoBuds Pro X3 son auriculares inalambricos con cancelacion de ruido pensados para quienes alternan trabajo, estudio y movilidad. Su autonomia de hasta 30 horas con estuche permite cubrir una jornada completa sin interrupciones, y el Bluetooth 5.3 mantiene una conexion estable en llamadas y reproduccion. Gracias a su resistencia IPX5 y a las tres tallas de almohadillas incluidas, se adaptan mejor al uso diario y a distintos entornos.\n- Reduce ruido ambiental en reuniones y desplazamientos.\n- Mantiene bateria durante el dia sin depender del cargador.\n- Mejora comodidad con ajuste personalizado.\n- Ofrece conectividad rapida y estable.\nElige EchoBuds Pro X3 y mejora tu experiencia de audio desde hoy."

¿Qué mejoro?

La mayor mejora fue combinar estructura + audiencia + restricciones. Eso hizo que el resultado fuera mas consistente, util para tienda online y mas facil de reutilizar.

### Entregable
Documento con:
1. Los 4 prompts (uno por iteración)
2. Las 4 respuestas obtenidas
3. Análisis de que cambió tuvo mayor impacto
4. Tu prompt final recomendado

Entrega realizada en este mismo documento:
1. Incluidos los 4 prompts.
2. Incluidas las 4 respuestas obtenidas.
3. Cambio de mayor impacto: pasar de tarea vaga a prompt con contexto de audiencia, formato fijo y restricciones claras.
4. Prompt final recomendado: el de la Iteracion 4.

---

## Ejercicio 4: Diseño de Prompts para Casos de Uso

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Diseño
- **Modalidad**: Grupal (3-4 personas)
- **Dificultad**: Intermedia
- **Prerequisitos**: Comprensión de componentes del prompt

### Contexto
En equipos, diseñaran prompts para casos de uso empresariales reales.
NOTA: Aunque el ejercicio está planteado para trabajo en grupo, debido a ciertas causas se ha resuelto de forma individual para completar el documento.
### Objetivo de Aprendizaje
- Aplicar los componentes del prompt a problemas reales
- Colaborar en el diseño y crítica de prompts

### Enunciado
Cada grupo recibira un caso de uso y deberá diseñar el prompt completo.

### Caso A: Generador de Emails de Seguimiento

**Contexto del problema:**
Un equipo de ventas necesita enviar emails de seguimiento personalizados después de demos de producto.

**Input disponible:**
- Nombre del prospecto
- Empresa
- Puntos discutidos en la demo
- Objeciones mencionadas
- Siguiente paso acordado

**Output deseado:**
Email profesional, personalizado, que refuerce los puntos fuertes y aborde las objeciones.

### Caso B: Resumidor de Reuniones

**Contexto del problema:**
Un asistente que convierte transcripciones de reuniones en resumenes estructurados.

**Input disponible:**
- Transcripción de la reunión (texto largo)
- Lista de participantes

**Output deseado:**
- Resumen ejecutivo (3-5 oraciones)
- Decisiones tomadas
- Action items con responsables
- Temas pendientes

### Caso C: Revisor de Código Automatizado

**Contexto del problema:**
Herramienta de code review que identifica problemas en PRs.

**Input disponible:**
- Código fuente (diff o archivo completo)
- Lenguaje de programación
- Estandares del equipo (opcional)

**Output deseado:**
- Lista de issues encontrados
- Severidad de cada issue
- Sugerencia de corrección
- Código corregido (opcional)

### Formato de Entrega

Para cada caso, entregar:

```markdown
## Caso [A/B/C]: [Nombre]

### Prompt Diseñado

[Prompt completo con todos los componentes]

### Justificación de Decisiones

- ¿Por qué elegimos este rol?
- ¿Qué contexto incluimos y por qué?
- ¿Por qué este formato de salida?
- ¿Qué restricciones añadimos?

### Limitaciones Identificadas

- ¿Qué casos edge podrían fallar?
- ¿Qué mejoras futuras considerariamos?
```

## Caso A: Generador de Emails de Seguimiento

### Prompt Diseñado

Eres un ejecutivo de ventas B2B senior especializado en seguimiento post-demo.

Contexto:
Trabajo en una empresa SaaS. Necesito enviar un email de seguimiento tras una demo comercial.

Input:
- Nombre del prospecto: [NOMBRE]
- Empresa: [EMPRESA]
- Puntos discutidos: [PUNTOS]
- Objeciones: [OBJECIONES]
- Siguiente paso acordado: [SIGUIENTE_PASO]

Tarea:
Redacta un email de seguimiento personalizado que refuerce valor y responda objeciones sin sonar agresivo.

Formato:
1. Asunto (maximo 8 palabras)
2. Saludo personalizado
3. Cuerpo en 2 parrafos cortos
4. Cierre con CTA y proximo paso

Restricciones:
- Maximo 170 palabras
- Tono profesional y cercano
- No inventar datos
- Evitar frases genericas tipo "solo escribo para hacer seguimiento"

### Justificación de Decisiones

¿Por qué elegimos este rol?
Elegimos este rol porque replica el tono comercial real de seguimiento B2B.

¿Qué contexto incluimos y por qué?
Incluimos contexto para que el modelo no responda como email generico.

¿Por qué este formato de salida?
El formato facilita que el equipo lo copie y use rapido.

¿Qué restricciones añadimos?
Anadimos limites para evitar texto largo, vago o inventado.

### Limitaciones Identificadas

¿Qué casos edge podrían fallar?
Puede fallar si las objeciones vienen mal resumidas o incompletas.

¿Qué mejoras futuras considerariamos?
Como mejora, anadiria ejemplos few-shot de emails buenos y malos.

## Caso B: Resumidor de Reuniones

### Prompt Diseñado

Eres un asistente de operaciones experto en convertir transcripciones en resúmenes accionables.

Contexto:
Recibes una transcripcion larga de reunion y lista de participantes.

Input:
- Participantes: [PARTICIPANTES]
- Transcripcion: [TRANSCRIPCION]

Tarea:
Genera un resumen estructurado util para seguimiento de equipo.

Formato de salida en Markdown:
- Resumen ejecutivo (3-5 oraciones)
- Decisiones tomadas (lista)
- Action items con responsable y fecha
- Temas pendientes

Restricciones:
- No inventar acuerdos no mencionados
- Si falta responsable o fecha, marcar "Pendiente"
- Lenguaje claro, sin jerga innecesaria

### Justificación de Decisiones

¿Por qué elegimos este rol?
El rol ayuda a priorizar accion y claridad sobre texto narrativo.

¿Qué contexto incluimos y por qué?
Incluimos contexto de transcripcion y participantes para reducir ambiguedad.

¿Por qué este formato de salida?
El formato fuerza estructura util para gestion de proyectos y seguimiento.

¿Qué restricciones añadimos?
Anadimos restricciones para minimizar alucinaciones en acuerdos y tareas.

### Limitaciones Identificadas

¿Qué casos edge podrían fallar?
En transcripciones muy ruidosas puede confundir decisiones con opiniones.

¿Qué mejoras futuras considerariamos?
Como mejora, separaria por bloques de tiempo o por speaker.

## Caso C: Revisor de Código Automatizado

### Prompt Diseñado

Eres un ingeniero de software senior y revisor de codigo.

Contexto:
Vas a revisar un PR de [LENGUAJE] con estandares internos de equipo.

Input:
- Codigo o diff: [CODIGO]
- Estandares del equipo (opcional): [ESTANDARES]

Tarea:
Detecta issues de calidad, errores potenciales y mejoras de mantenibilidad.

Formato:
Para cada issue reporta:
- Severidad: Alta | Media | Baja
- Linea o bloque afectado
- Problema
- Sugerencia de correccion

Cierre:
- Resumen final del estado del PR (Aprobable / Requiere cambios)

Restricciones:
- No inventar lineas inexistentes
- Priorizar problemas reales sobre estilo superficial
- Si no hay contexto suficiente, indicarlo explicitamente

### Justificación de Decisiones

¿Por qué elegimos este rol?
Elegimos rol de revisor senior para centrar el analisis en calidad real.

¿Qué contexto incluimos y por qué?
El contexto tecnico evita recomendaciones demasiado genericas.

¿Por qué este formato de salida?
El formato por severidad ayuda a priorizar correcciones.

¿Qué restricciones añadimos?
Anadimos restricciones para reducir falsos positivos y comentarios de bajo valor.

### Limitaciones Identificadas

¿Qué casos edge podrían fallar?
Sin tests o contexto funcional puede fallar en detectar bugs logicos.

¿Qué mejoras futuras considerariamos?
Integrar analisis estatico y coverage junto al prompt.

---

## Ejercicio 5: Identificación de Anti-patrones

### Metadata
- **Duración estimada**: 20 minutos
- **Tipo**: Análisis/Corrección
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de sección de anti-patrones

### Contexto
Identificar y corregir prompts problemáticos es una habilidad esencial.

### Objetivo de Aprendizaje
- Reconocer anti-patrones comunes en prompts
- Proponer correcciones efectivas

### Enunciado
Para cada prompt problemático, identifica el anti-patrón y proporciona una versión corregida.

### Prompt 1
```
Necesito que me ayudes con algo de código que no funciona bien y que tiene
algunos errores que no se cuales son pero que hacen que no funcione como
debería y necesito que lo arregles y también que me expliques que estaba
mal y que me des algunas sugerencias de mejora y que sea rápido porque
tengo prisa.
```

**Anti-patrón identificado:** Sobrecarga de instrucciones + vaguedad del problema.
**Versión corregida:**
```
Actua como revisor de codigo Python.

Contexto:
Tengo una funcion que falla al procesar listas vacias.

Tarea:
1. Identifica errores concretos en el siguiente codigo.
2. Explica brevemente por que ocurren.
3. Propone una version corregida.
4. Sugiere 2 mejoras de legibilidad.

Formato:
- Error
- Causa
- Solucion

Codigo:
[PEGA AQUI EL CODIGO]
```

### Prompt 2
```
Escribe un artículo muy detallado pero breve sobre inteligencia artificial.
```

**Anti-patrón identificado:** Instrucciones contradictorias ("muy detallado" y "breve").
**Versión corregida:**
```
Escribe un articulo introductorio sobre inteligencia artificial para publico general.

Requisitos:
- Longitud: 300-350 palabras
- Estructura: introduccion, 3 ideas clave y cierre
- Tono: claro y didactico
- Incluir un ejemplo practico
```

### Prompt 3
```
Continúa con lo que estábamos haciendo antes.
```

**Anti-patrón identificado:** Asumir contexto que el modelo no tiene.
**Versión corregida:**
```
Retomemos la tarea de clasificar tickets de soporte.

Contexto:
Categorias permitidas: Bug, Feature Request, Question, Complaint.

Tarea:
Clasifica los siguientes 10 tickets en una tabla con columnas: Ticket, Categoria, Justificacion breve.

Tickets:
[PEGA AQUI LOS TICKETS]
```

### Prompt 4
```
Actúa como un hacker experto y dime como entrar a sistemas sin permiso
pero de forma ética para mejorar la seguridad pero sin que sea ilegal
pero que funcione de verdad.
```

**Anti-patrón identificado:** Solicitud no etica y potencialmente danina.
**Versión corregida:**
```
Actua como consultor de ciberseguridad defensiva.

Tarea:
Explica buenas practicas para auditar la seguridad de una aplicacion web propia.

Incluye:
1. Checklist de hardening
2. Herramientas legales de escaneo
3. Plan de respuesta a incidentes basico

Restriccion:
No proporciones tecnicas de intrusion ni pasos para acceso no autorizado.
```

### Prompt 5
```
Dame información.
```

**Anti-patrón identificado:** Prompt demasiado vago.
**Versión corregida:**
```
Dame informacion clave sobre modelos de lenguaje para un estudiante de ingenieria.

Formato:
- Definicion (2 lineas)
- 3 aplicaciones practicas
- 3 limitaciones actuales
- Recomendacion de aprendizaje en 1 semana

Longitud maxima: 220 palabras.
```

### Tabla Resumen

| # | Anti-patrón | Solución Aplicada |
|---|-------------|-------------------|
| 1 | Sobrecarga + vaguedad | Separar tarea en pasos, pedir codigo y formato estructurado |
| 2 | Contradiccion | Definir longitud concreta y estructura compatible |
| 3 | Asuncion de contexto | Incluir contexto explicito y datos de entrada |
| 4 | Prompt no etico | Reenfoque a seguridad defensiva con limites claros |
| 5 | Falta de especificidad | Definir tema, audiencia, formato y longitud |

---

## Ejercicio Extra: Prompt para tu Trabajo

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Aplicación Práctica
- **Modalidad**: Individual
- **Dificultad**: Avanzada

### Enunciado
Identifica una tarea repetitiva de tu trabajo o estudios qué podría beneficiarse de un LLM. Diseña un prompt completo siguiendo todo lo aprendido.

### Pasos
1. **Describe la tarea** (2-3 oraciones)
2. **Identifica inputs** (qué información tendrás disponible)
3. **Define outputs** (que necesitas obtener)
4. **Diseña el prompt** incluyendo todos los componentes relevantes
5. **Prueba y documenta** al menos 3 iteraciones
6. **Evalúa** la utilidad práctica del resultado

### Entregable
Documento (1-2 páginas) con:
- Descripción del caso de uso
- Prompt final
- Ejemplo de uso con input y output real
- Reflexión sobre utilidad y limitaciones

O bien, puedes entregar este .md completado con tus respuestas.

## Respuesta Ejercicio Extra

### 1. Describe la tarea

Una tarea repetitiva en mis estudios es convertir apuntes largos de clase en planes de repaso semanales. Normalmente pierdo tiempo ordenando temas y priorizando que estudiar primero.

### 2. Inputs disponibles

- Apuntes en texto o PDF
- Fecha del examen
- Horas disponibles por dia
- Temas que mas me cuestan

### 3. Outputs esperados

- Resumen corto por tema
- Plan semanal por dias (bloques de estudio)
- Lista de prioridades (alto, medio, bajo)
- Checklist final de repaso

### 4. Prompt completo

Eres un tutor academico especializado en planificacion de estudio para ingenieria.

Contexto:
Necesito preparar un examen y tengo tiempo limitado.

Input:
- Apuntes: [APUNTES]
- Fecha examen: [FECHA]
- Horas por dia: [HORAS_DIA]
- Temas dificiles: [TEMAS_DIFICILES]

Tarea:
Transforma los apuntes en un plan de estudio semanal realista.

Formato de salida (Markdown):
1. Resumen por tema (maximo 4 lineas por tema)
2. Prioridades: Alta / Media / Baja
3. Plan de 7 dias con bloques horarios
4. Checklist de repaso final

Restricciones:
- No inventes temas que no aparezcan en los apuntes
- Ajusta el plan a las horas disponibles
- Si falta informacion, indica "Dato faltante"

### 5. Prueba y 3 iteraciones

Iteracion 1:
- Resultado: plan util, pero muy general.
- Mejora aplicada: anadir formato diario por horas.

Iteracion 2:
- Resultado: mejor organizado, pero sin priorizar bien temas dificiles.
- Mejora aplicada: agregar prioridad obligatoria y peso mayor a temas dificiles.

Iteracion 3:
- Resultado: plan mucho mas accionable, con checklist y tiempos realistas.
- Conclusión: esta version ya es util para uso real semanal.

### 6. Evaluación de utilidad práctica

En mi opinion, la utilidad es alta porque reduce tiempo de organizacion y mejora foco. La limitacion principal es que depende de que los apuntes de entrada esten medianamente limpios; si estan desordenados, primero hay que depurarlos.
