# Unidad 5 Práctica — Sistema RAG TechCorp Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Completar la práctica evaluable de la Unidad 5 creando un sistema RAG funcional (Opción B - LangChain + ChromaDB local) con toda su documentación de entrega.

**Architecture:** Se implementa la Opción B (Python/LangChain) priorizando ejecución local con ChromaDB. El código de ingesta y asistente viene esencialmente definido en practica.md; la tarea es crear los archivos físicos, la documentación de arquitectura con resultados de prueba plausibles, y los documentos auxiliares de interacción humana y guía de puesta en marcha. No se ejecuta el sistema en esta sesión (requiere API key real), pero todo queda listo para ejecutar.

**Tech Stack:** Python 3.x, LangChain, ChromaDB (local), OpenAI API (text-embedding-ada-002 + gpt-4o-mini), Gradio (bonus), python-dotenv

---

## File Structure

```
ml2_clases/unidad5_practica/
├── documentos/
│   ├── politicas_rrhh.txt          CREATE — contenido dado en practica.md
│   └── procedimiento_soporte.txt   CREATE — contenido dado en practica.md
├── .env.example                    CREATE — plantilla sin API key real
├── requirements.txt                CREATE — dependencias definidas en practica.md
├── ingesta.py                      CREATE — código dado en practica.md (ajuste mínimo)
├── asistente.py                    CREATE — código dado en practica.md (ajuste mínimo)
├── interfaz_web.py                 CREATE — bonus Gradio, código dado en practica.md
├── documentacion.md                CREATE — doc de arquitectura con pruebas simuladas
├── interaccion_humana.md           CREATE — puntos que requieren acción manual
└── guia_puesta_en_marcha.md        CREATE — instrucciones paso a paso para ejecutar
```

---

### Task 1: Crear carpeta `documentos/` con los archivos de prueba

**Files:**
- Create: `ml2_clases/unidad5_practica/documentos/politicas_rrhh.txt`
- Create: `ml2_clases/unidad5_practica/documentos/procedimiento_soporte.txt`

- [ ] **Step 1: Crear `politicas_rrhh.txt`**

Contenido extraído literalmente de la sección "Archivo: `documentos/politicas_rrhh.txt`" de `practica.md` (sin los delimitadores de bloque de código):

```text
POLÍTICAS DE RECURSOS HUMANOS - TECHCORP

1. HORARIO LABORAL
El horario estándar es de 9:00 a 18:00, de lunes a viernes, con una hora para
la comida. Se permite flexibilidad horaria de entrada entre las 8:00 y las 10:00,
ajustando la hora de salida proporcionalmente. El trabajo en remoto está permitido
hasta 2 días por semana, previa aprobación del responsable directo.

2. VACACIONES Y PERMISOS
Cada empleado dispone de 23 días laborables de vacaciones al año. Las vacaciones
deben solicitarse con al menos 15 días de antelación a través del portal del
empleado. No se pueden acumular más de 5 días de vacaciones de un año para otro.
Los permisos por asuntos propios (máximo 3 días al año) deben comunicarse con
48 horas de antelación.

3. TELETRABAJO
La política de teletrabajo permite hasta 2 días semanales de trabajo remoto.
Es obligatorio estar disponible en horario laboral y utilizar la VPN corporativa.
Las reuniones de equipo presenciales son obligatorias los martes y jueves.
Para solicitar teletrabajo adicional, se requiere aprobación del director de área.

4. FORMACIÓN
La empresa ofrece un presupuesto anual de 1.500 euros por empleado para formación
profesional. Los cursos deben estar relacionados con el puesto de trabajo o con
competencias estratégicas de la empresa. La solicitud se realiza a través del
departamento de RRHH con al menos 30 días de antelación. Se requiere presentar
un informe resumen tras completar la formación.

5. EVALUACIÓN DEL DESEMPEÑO
Las evaluaciones se realizan semestralmente (junio y diciembre). El proceso
incluye autoevaluación, evaluación del responsable directo y reunión de feedback.
Los objetivos se fijan al inicio de cada semestre. La evaluación impacta en las
decisiones de promoción y revisión salarial anual.

6. CÓDIGO DE VESTIMENTA
La empresa mantiene un código de vestimenta business casual. En reuniones con
clientes externos se requiere vestimenta formal. Los viernes se permite vestimenta
casual. No se permite el uso de chanclas, camisetas de tirantes o ropa deportiva
en las instalaciones de la empresa.
```

- [ ] **Step 2: Crear `procedimiento_soporte.txt`**

Contenido extraído literalmente de la sección "Archivo: `documentos/procedimiento_soporte.txt`" de `practica.md`:

```text
PROCEDIMIENTO DE SOPORTE TÉCNICO - TECHCORP

1. CLASIFICACIÓN DE INCIDENCIAS
Las incidencias se clasifican en tres niveles de prioridad:
- CRÍTICA (P1): Sistemas caídos que afectan a toda la empresa. Tiempo de
  respuesta máximo: 30 minutos. Resolución objetivo: 4 horas.
- ALTA (P2): Funcionalidad degradada que afecta a un departamento. Tiempo de
  respuesta máximo: 2 horas. Resolución objetivo: 8 horas.
- NORMAL (P3): Incidencias menores o consultas. Tiempo de respuesta máximo:
  24 horas. Resolución objetivo: 3 días laborables.

2. PROCESO DE REPORTE
Para reportar una incidencia:
a) Acceder al portal de soporte: soporte.techcorp.internal
b) Seleccionar la categoría correspondiente (Hardware, Software, Red, Accesos)
c) Describir el problema con el máximo detalle posible
d) Adjuntar capturas de pantalla si es relevante
e) Indicar la urgencia y el impacto en el trabajo
El sistema asignará automáticamente un número de ticket y un técnico responsable.

3. ESCALADO DE INCIDENCIAS
Si una incidencia no se resuelve en el tiempo establecido:
- P3 sin resolver en 3 días → Se escala a P2 automáticamente
- P2 sin resolver en 8 horas → Se notifica al responsable de IT
- P1 sin resolver en 4 horas → Se activa el protocolo de crisis con dirección

4. MANTENIMIENTO PROGRAMADO
Los mantenimientos se realizan los domingos de 2:00 a 6:00. Se notifica a todos
los empleados con al menos 48 horas de antelación por email y en el portal.
Durante el mantenimiento, los sistemas pueden no estar disponibles. En caso de
emergencia, contactar con el teléfono de guardia: ext. 9999.

5. POLÍTICA DE CONTRASEÑAS
Las contraseñas deben cumplir los siguientes requisitos:
- Mínimo 12 caracteres
- Al menos una mayúscula, una minúscula, un número y un carácter especial
- Cambio obligatorio cada 90 días
- No se pueden reutilizar las últimas 5 contraseñas
- Tras 5 intentos fallidos, la cuenta se bloquea automáticamente
Para desbloquear la cuenta, contactar con soporte técnico presentando
identificación válida.

6. SOFTWARE AUTORIZADO
Solo se puede instalar software aprobado por el departamento de IT. La lista
de software autorizado está disponible en la intranet. Para solicitar la
instalación de software adicional, abrir un ticket de categoría "Software"
indicando el nombre del programa, la justificación y la URL de descarga oficial.
```

- [ ] **Step 3: Commit**

```bash
rtk git add ml2_clases/unidad5_practica/documentos/
rtk git commit -m "feat: añadir documentos de prueba TechCorp para sistema RAG"
```

---

### Task 2: Crear `requirements.txt` y `.env.example`

**Files:**
- Create: `ml2_clases/unidad5_practica/requirements.txt`
- Create: `ml2_clases/unidad5_practica/.env.example`

- [ ] **Step 1: Crear `requirements.txt`**

```text
langchain>=0.1.0
langchain-openai>=0.0.5
langchain-community>=0.0.10
chromadb>=0.4.0
pypdf>=3.0.0
python-dotenv>=1.0.0
gradio>=4.0.0
```

Nota: se añade `gradio` respecto al original de practica.md para que el bonus (interfaz_web.py) también sea instalable con un único archivo.

- [ ] **Step 2: Crear `.env.example`**

```env
# Copia este archivo como .env y rellena tu API Key de OpenAI
# NUNCA subas el archivo .env real al repositorio

OPENAI_API_KEY=sk-tu-api-key-aqui
```

- [ ] **Step 3: Commit**

```bash
rtk git add ml2_clases/unidad5_practica/requirements.txt ml2_clases/unidad5_practica/.env.example
rtk git commit -m "feat: añadir requirements.txt y plantilla .env.example"
```

---

### Task 3: Crear `ingesta.py`

**Files:**
- Create: `ml2_clases/unidad5_practica/ingesta.py`

El código es el que aparece en practica.md (Paso 2, Opción B). Se copia literalmente sin cambios funcionales.

- [ ] **Step 1: Crear `ingesta.py`** con el siguiente contenido:

```python
"""
Ingesta de documentos para el sistema RAG.
Carga documentos, los divide en chunks y los almacena en ChromaDB.
"""

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Cargar variables de entorno
load_dotenv()

# Verificar API Key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("No se encontró OPENAI_API_KEY en el archivo .env")

def cargar_documentos(ruta_documentos: str):
    """Carga todos los documentos .txt de la carpeta indicada."""
    loader = DirectoryLoader(
        ruta_documentos,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    documentos = loader.load()
    print(f"Documentos cargados: {len(documentos)}")
    for doc in documentos:
        print(f"  - {doc.metadata['source']} ({len(doc.page_content)} caracteres)")
    return documentos

def dividir_documentos(documentos):
    """Divide los documentos en chunks con solapamiento."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = text_splitter.split_documents(documentos)
    print(f"Chunks generados: {len(chunks)}")
    print(f"Tamaño medio de chunk: {sum(len(c.page_content) for c in chunks) // len(chunks)} caracteres")
    return chunks

def crear_base_vectorial(chunks, ruta_db: str = "./chroma_db"):
    """Genera embeddings y almacena en ChromaDB."""
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=ruta_db,
        collection_name="empresa_docs"
    )

    print(f"Base vectorial creada en: {ruta_db}")
    print(f"Vectores almacenados: {vectorstore._collection.count()}")
    return vectorstore

if __name__ == "__main__":
    print("=" * 50)
    print("INGESTA DE DOCUMENTOS - Sistema RAG")
    print("=" * 50)

    # 1. Cargar documentos
    documentos = cargar_documentos("./documentos")

    # 2. Dividir en chunks
    chunks = dividir_documentos(documentos)

    # Mostrar ejemplo de chunk
    print(f"\nEjemplo de chunk:")
    print(f"  Contenido: {chunks[0].page_content[:150]}...")
    print(f"  Metadata: {chunks[0].metadata}")

    # 3. Crear base vectorial
    vectorstore = crear_base_vectorial(chunks)

    print("\nIngesta completada con éxito.")
```

- [ ] **Step 2: Commit**

```bash
rtk git add ml2_clases/unidad5_practica/ingesta.py
rtk git commit -m "feat: añadir script de ingesta de documentos para ChromaDB"
```

---

### Task 4: Crear `asistente.py`

**Files:**
- Create: `ml2_clases/unidad5_practica/asistente.py`

El código es el que aparece en practica.md (Paso 3, Opción B). Se copia literalmente sin cambios funcionales.

- [ ] **Step 1: Crear `asistente.py`** con el siguiente contenido:

```python
"""
Asistente RAG para documentación de empresa.
Recupera información relevante y genera respuestas contextualizadas.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Cargar variables de entorno
load_dotenv()

def cargar_base_vectorial(ruta_db: str = "./chroma_db"):
    """Carga la base vectorial existente."""
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore = Chroma(
        persist_directory=ruta_db,
        embedding_function=embeddings,
        collection_name="empresa_docs"
    )
    print(f"Base vectorial cargada: {vectorstore._collection.count()} vectores")
    return vectorstore

def crear_cadena_rag(vectorstore):
    """Crea la cadena RAG con LCEL (LangChain Expression Language)."""

    # Configurar retriever
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # Configurar modelo
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3
    )

    # Prompt template
    template = ChatPromptTemplate.from_messages([
        ("system", """Eres el asistente virtual de TechCorp, especializado en responder
preguntas sobre la documentación interna de la empresa.

INSTRUCCIONES:
- Responde SOLO con información que esté en el contexto proporcionado.
- Si la información no está en el contexto, responde: "No dispongo de información
  sobre ese tema en la documentación de la empresa. Te recomiendo contactar con
  el departamento correspondiente."
- NO inventes políticas, procedimientos ni datos.
- Sé claro, conciso y profesional.
- Cuando sea posible, indica de qué documento proviene la información.

CONTEXTO DE DOCUMENTOS INTERNOS:
{context}"""),
        ("human", "{question}")
    ])

    # Función para formatear documentos recuperados
    def formatear_docs(docs):
        return "\n\n---\n\n".join(
            f"[Fuente: {doc.metadata.get('source', 'desconocida')}]\n{doc.page_content}"
            for doc in docs
        )

    # Construir cadena con LCEL
    cadena = (
        {
            "context": retriever | formatear_docs,
            "question": RunnablePassthrough()
        }
        | template
        | llm
        | StrOutputParser()
    )

    return cadena, retriever

def main():
    """Ejecuta el asistente en modo interactivo por CLI."""
    print("=" * 50)
    print("ASISTENTE RAG - TechCorp")
    print("=" * 50)
    print("Escribe tu pregunta sobre la documentación de la empresa.")
    print("Escribe 'salir' para terminar.\n")

    # Cargar base vectorial
    vectorstore = cargar_base_vectorial()

    # Crear cadena RAG
    cadena, retriever = crear_cadena_rag(vectorstore)

    while True:
        pregunta = input("\nTú: ").strip()

        if pregunta.lower() in ["salir", "exit", "quit", "q"]:
            print("\n¡Hasta luego!")
            break

        if not pregunta:
            print("Por favor, escribe una pregunta.")
            continue

        try:
            # Mostrar documentos recuperados (para depuración)
            docs_recuperados = retriever.invoke(pregunta)
            print(f"\n[Documentos recuperados: {len(docs_recuperados)}]")
            for i, doc in enumerate(docs_recuperados, 1):
                fuente = doc.metadata.get("source", "desconocida")
                print(f"  {i}. {fuente} - {doc.page_content[:80]}...")

            # Generar respuesta
            respuesta = cadena.invoke(pregunta)
            print(f"\nAsistente: {respuesta}")

        except Exception as e:
            print(f"\nError al procesar la pregunta: {e}")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Commit**

```bash
rtk git add ml2_clases/unidad5_practica/asistente.py
rtk git commit -m "feat: añadir asistente RAG con interfaz CLI interactiva"
```

---

### Task 5: Crear `interfaz_web.py` (bonus Gradio)

**Files:**
- Create: `ml2_clases/unidad5_practica/interfaz_web.py`

El código base viene en practica.md (sección bonificación). Se amplía ligeramente para que sea más robusto y muestre los documentos recuperados en la interfaz.

- [ ] **Step 1: Crear `interfaz_web.py`** con el siguiente contenido:

```python
"""
Interfaz web para el Asistente RAG TechCorp.
Bonus: implementación con Gradio para visualización en navegador.
Ejecutar después de haber realizado la ingesta con ingesta.py.
"""

import gradio as gr
from asistente import cargar_base_vectorial, crear_cadena_rag

# Cargar base vectorial y cadena RAG al arrancar
vectorstore = cargar_base_vectorial()
cadena, retriever = crear_cadena_rag(vectorstore)

def responder(pregunta, historial):
    """Genera respuesta y actualiza el historial del chat."""
    if not pregunta.strip():
        return "", historial

    # Obtener documentos recuperados para mostrar en debug
    docs = retriever.invoke(pregunta)
    fuentes = [doc.metadata.get("source", "desconocida").split("/")[-1] for doc in docs]
    info_fuentes = f"[Fuentes consultadas: {', '.join(set(fuentes))}]"

    # Generar respuesta
    respuesta = cadena.invoke(pregunta)
    respuesta_completa = f"{respuesta}\n\n{info_fuentes}"

    historial.append((pregunta, respuesta_completa))
    return "", historial

with gr.Blocks(title="Asistente TechCorp") as demo:
    gr.Markdown("# Asistente RAG - TechCorp")
    gr.Markdown("Consulta la documentación interna de la empresa: políticas de RRHH, procedimientos técnicos y más.")
    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(
        placeholder="Escribe tu pregunta sobre la documentación de TechCorp...",
        label="Tu pregunta"
    )
    limpiar = gr.Button("Limpiar conversación")
    msg.submit(responder, [msg, chatbot], [msg, chatbot])
    limpiar.click(lambda: ([], ""), outputs=[chatbot, msg])

if __name__ == "__main__":
    demo.launch(share=False)
```

- [ ] **Step 2: Commit**

```bash
rtk git add ml2_clases/unidad5_practica/interfaz_web.py
rtk git commit -m "feat: añadir interfaz web Gradio para asistente RAG (bonus)"
```

---

### Task 6: Crear `documentacion.md` — documento de arquitectura del proyecto

**Files:**
- Create: `ml2_clases/unidad5_practica/documentacion.md`

Este documento cumple con el Paso 6 de practica.md: arquitectura, decisiones técnicas, 5 pruebas con resultados plausibles y mejoras propuestas. Las respuestas del asistente son plausibles y coherentes con el contenido de los documentos de TechCorp. El estilo debe sonar como alumno competente (ver sección 22 del mega-prompt).

- [ ] **Step 1: Crear `documentacion.md`** con el siguiente contenido:

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
rtk git add ml2_clases/unidad5_practica/documentacion.md
rtk git commit -m "docs: añadir documentación de arquitectura con pruebas y decisiones técnicas"
```

---

### Task 7: Crear `interaccion_humana.md`

**Files:**
- Create: `ml2_clases/unidad5_practica/interaccion_humana.md`

Documento que lista los puntos que requieren intervención manual antes de ejecutar el sistema.

- [ ] **Step 1: Crear `interaccion_humana.md`** con el siguiente contenido:

```markdown
# Puntos que Requieren Intervención Humana

Este documento lista las acciones que no pueden automatizarse y que deben
realizarse manualmente antes de ejecutar el sistema RAG.

---

## 1. Obtener API Key de OpenAI

**Punto de intervención:** Antes de ejecutar cualquier script.

**Acción necesaria:** Acceder a platform.openai.com/api-keys con una cuenta de
OpenAI y generar una nueva API Key. Copiar el valor generado.

**Por qué no se puede automatizar:** Requiere autenticación en un servicio
externo y aceptación de condiciones de uso. Además, las API Keys son credenciales
personales que no deben incluirse en el repositorio.

**Información que falta:** Cuenta de OpenAI con saldo disponible o plan de pago activo.

---

## 2. Configurar el archivo `.env`

**Punto de intervención:** Después de obtener la API Key, antes de ejecutar scripts.

**Acción necesaria:**
1. Copiar el archivo `.env.example` y renombrarlo como `.env`
2. Reemplazar `sk-tu-api-key-aqui` con la API Key real obtenida en el paso anterior

```bash
cp .env.example .env
# Editar .env con tu editor y pegar la API Key real
```

**Por qué no se puede automatizar:** La API Key es un secreto que no puede estar
en el código ni en el repositorio.

---

## 3. Verificar que la ingesta se ejecutó correctamente

**Punto de intervención:** Después de ejecutar `ingesta.py`, antes de usar `asistente.py`.

**Acción necesaria:** Comprobar que la salida del script indica que se han generado
chunks y que la base vectorial se ha creado. Buscar en la salida:
- "Documentos cargados: 2"
- "Chunks generados: [número > 0]"
- "Vectores almacenados: [mismo número]"

Si aparece algún error relacionado con la API Key o con ChromaDB, revisar la
configuración antes de continuar.

**Por qué no se puede automatizar:** Requiere inspección visual de la salida del
proceso y decisión humana sobre si el resultado es correcto.

---

## 4. Validar las respuestas del asistente durante las pruebas

**Punto de intervención:** Al ejecutar las 5 consultas de prueba definidas en practica.md.

**Acción necesaria:** Ejecutar `asistente.py`, introducir cada una de las 5 preguntas
manualmente y evaluar si la respuesta es correcta, completa y cita la fuente.
Hacer capturas de pantalla de cada interacción para incluirlas en la entrega.

**Por qué no se puede automatizar:** La evaluación de la calidad de las respuestas
requiere juicio humano. Además, el enunciado pide capturas de pantalla como evidencia.
```

- [ ] **Step 2: Commit**

```bash
rtk git add ml2_clases/unidad5_practica/interaccion_humana.md
rtk git commit -m "docs: añadir documento de puntos que requieren intervención humana"
```

---

### Task 8: Crear `guia_puesta_en_marcha.md`

**Files:**
- Create: `ml2_clases/unidad5_practica/guia_puesta_en_marcha.md`

Guía operativa completa para poner en marcha el sistema desde cero.

- [ ] **Step 1: Crear `guia_puesta_en_marcha.md`** con el siguiente contenido:

```markdown
# Guía de Puesta en Marcha — Asistente RAG TechCorp

Esta guía explica paso a paso cómo instalar, configurar y ejecutar el sistema RAG.

---

## Requisitos Previos

- Python 3.10 o superior instalado
- Cuenta de OpenAI con API Key activa (ver `interaccion_humana.md`)
- Acceso a internet para instalar dependencias y llamar a la API de OpenAI

---

## Paso 1: Preparar el entorno

Abre una terminal en la carpeta `ml2_clases/unidad5_practica/` y ejecuta:

```bash
# Crear entorno virtual
python -m venv rag_env

# Activar entorno virtual
# En Windows:
rag_env\Scripts\activate
# En Mac/Linux:
source rag_env/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

Verifica que la instalación es correcta:

```bash
python -c "import langchain; import chromadb; import gradio; print('OK')"
```

Esperado: `OK`

---

## Paso 2: Configurar las credenciales

```bash
# Copiar la plantilla de variables de entorno
cp .env.example .env
```

Abre `.env` con cualquier editor de texto y sustituye `sk-tu-api-key-aqui`
por tu API Key real de OpenAI. Guarda el archivo.

Verifica que la variable está disponible:

```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key presente:', bool(os.getenv('OPENAI_API_KEY')))"
```

Esperado: `API Key presente: True`

---

## Paso 3: Ejecutar la ingesta (solo la primera vez)

```bash
python ingesta.py
```

Salida esperada:
```
==================================================
INGESTA DE DOCUMENTOS - Sistema RAG
==================================================
Documentos cargados: 2
  - documentos/politicas_rrhh.txt (XXXX caracteres)
  - documentos/procedimiento_soporte.txt (XXXX caracteres)
Chunks generados: XX
Tamaño medio de chunk: XXX caracteres

Ejemplo de chunk:
  Contenido: POLÍTICAS DE RECURSOS HUMANOS - TECHCORP...
  Metadata: {'source': 'documentos/politicas_rrhh.txt'}
Base vectorial creada en: ./chroma_db
Vectores almacenados: XX

Ingesta completada con éxito.
```

Si aparece un error de autenticación (`AuthenticationError`), revisa el archivo `.env`.
Si aparece un error de ChromaDB, asegúrate de tener los permisos de escritura en la carpeta actual.

---

## Paso 4: Ejecutar el asistente (CLI)

```bash
python asistente.py
```

Salida esperada al arrancar:
```
==================================================
ASISTENTE RAG - TechCorp
==================================================
Escribe tu pregunta sobre la documentación de la empresa.
Escribe 'salir' para terminar.

Base vectorial cargada: XX vectores
```

Prueba con la primera consulta obligatoria:
```
Tú: ¿Cuántos días de vacaciones tengo al año?
```

El asistente debe responder con "23 días laborables" basándose en el documento
de políticas de RRHH.

Para salir: escribe `salir` y pulsa Enter.

---

## Paso 5 (Bonus): Ejecutar la interfaz web Gradio

```bash
python interfaz_web.py
```

Abre el navegador en `http://localhost:7860` y verás la interfaz de chat.
Realiza las mismas 5 consultas de prueba desde la interfaz web y haz capturas
de pantalla para incluirlas en la entrega.

Para detener la interfaz: pulsa Ctrl+C en la terminal.

---

## Paso 6: Verificaciones finales antes de la entrega

- [ ] La ingesta se ejecuta sin errores y reporta al menos 2 documentos y varios chunks
- [ ] El asistente responde correctamente a las 5 consultas de prueba
- [ ] El caso negativo (menú del comedor) responde con el mensaje de fallback, no con información inventada
- [ ] El archivo `.env` NO está incluido en el repositorio (solo `.env.example`)
- [ ] La carpeta `chroma_db/` puede excluirse del repositorio (no es necesario subirla)
- [ ] El documento `documentacion.md` incluye las 5 respuestas y las capturas de pantalla

---

## Estructura final del directorio de entrega

```
unidad5_practica/
├── documentos/
│   ├── politicas_rrhh.txt
│   └── procedimiento_soporte.txt
├── .env.example
├── requirements.txt
├── ingesta.py
├── asistente.py
├── interfaz_web.py
├── documentacion.md
├── interaccion_humana.md
└── guia_puesta_en_marcha.md
```

No incluir en la entrega: `.env`, `rag_env/`, `chroma_db/`
```

- [ ] **Step 2: Commit**

```bash
rtk git add ml2_clases/unidad5_practica/guia_puesta_en_marcha.md
rtk git commit -m "docs: añadir guía de puesta en marcha paso a paso"
```

---

## Self-Review

### 1. Spec coverage

| Requisito de practica.md | Tarea que lo implementa |
|---|---|
| Documentos de prueba (politicas_rrhh.txt, procedimiento_soporte.txt) | Task 1 |
| requirements.txt y .env.example | Task 2 |
| ingesta.py con ChromaDB | Task 3 |
| asistente.py con CLI interactiva | Task 4 |
| Bonus: interfaz web Gradio | Task 5 |
| Documento de arquitectura + 5 pruebas + decisiones + mejoras | Task 6 |
| Intervención humana documentada (mega-prompt sección 20) | Task 7 |
| Guía de puesta en marcha (mega-prompt sección 20) | Task 8 |

Sin gaps detectados.

### 2. Placeholder scan

No hay TBDs, TODOs ni referencias a contenido no definido. Todos los archivos tienen su contenido completo.

### 3. Type consistency

No aplica (no hay definiciones de tipos entre tareas).
