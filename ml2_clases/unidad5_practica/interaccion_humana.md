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

---
