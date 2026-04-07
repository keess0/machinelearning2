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

---
