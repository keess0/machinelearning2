# Documentación - Servidor MCP para Gmail
## Práctica Unidad 6 - Model Context Protocol

**Autor:** Diego Keess Lambás  
**Fecha:** Abril 2026

---

## 1. Flujo OAuth 2.0 Implementado

La autenticación con Gmail utiliza el protocolo **OAuth 2.0** con el flujo de "Aplicación de escritorio" de Google. El proceso funciona de la siguiente manera:

### Primera ejecución
1. El servidor busca el archivo `token.json` en el directorio local.
2. Como no existe, lanza `InstalledAppFlow` que abre el navegador del sistema.
3. El usuario inicia sesión en Google y acepta los permisos solicitados (lectura, envío y modificación de Gmail).
4. Google devuelve un código de autorización que el flujo canjea por un **access token** y un **refresh token**.
5. Las credenciales se guardan en `token.json` para futuras ejecuciones.

### Ejecuciones posteriores
1. El servidor carga `token.json` con las credenciales previas.
2. Si el access token está vigente, lo usa directamente.
3. Si ha expirado, usa el refresh token para obtener uno nuevo de forma transparente, sin intervención del usuario.

### Scopes utilizados
| Scope | Propósito |
|-------|-----------|
| `gmail.readonly` | Leer emails de la bandeja de entrada |
| `gmail.send` | Enviar nuevos emails |
| `gmail.modify` | Modificar estado de emails (futuras extensiones) |

---

## 2. Componentes del Servidor MCP

El servidor está construido con **FastMCP**, una librería de alto nivel sobre el SDK oficial de MCP que simplifica la declaración de herramientas, recursos y prompts mediante decoradores Python.

### Tools (Herramientas)

Las herramientas son **acciones que el LLM puede ejecutar** en nombre del usuario. El LLM decide cuándo y cómo llamarlas basándose en la conversación.

#### `list_emails(max_results: int = 10)`
- **Qué hace:** Consulta la API de Gmail para obtener los mensajes más recientes de la bandeja de entrada (`INBOX`).
- **Proceso:** Primero obtiene una lista de IDs de mensajes, luego recupera los metadatos (remitente, asunto, fecha) de cada uno.
- **Retorna:** Texto formateado con los datos de cada email separados por `---`.

#### `send_email(to, subject, body)`
- **Qué hace:** Construye un mensaje MIME de texto plano, lo codifica en Base64 URL-safe (requerido por la API de Gmail) y lo envía.
- **Retorna:** Confirmación con el ID del mensaje enviado por Gmail.

### Resources (Recursos)

Los recursos son **datos que el LLM puede consultar** sin ejecutar una acción. Se identifican por una URI.

#### `gmail://profile`
- **Qué hace:** Llama al endpoint `users.getProfile` de Gmail API para obtener los datos del usuario autenticado.
- **Retorna:** Email, total de mensajes y total de hilos en la cuenta.

### Prompts (Plantillas)

Los prompts son **instrucciones reutilizables** que el LLM puede usar como punto de partida para tareas específicas.

#### `redactar_email(destinatario, tema, tono)`
- **Qué hace:** Genera una instrucción estructurada para que el LLM redacte un email con características específicas.
- **Parámetros:** Destinatario, tema del mensaje y tono deseado (profesional, informal o formal).

---

## 3. Dificultades Encontradas

### Gestión de rutas en Windows
La función `get_gmail_service()` usa `os.path.dirname(os.path.abspath(__file__))` para construir rutas absolutas a `credentials.json` y `token.json`. Esto garantiza que el servidor funcione independientemente del directorio de trabajo desde el que lo lance Claude Desktop.

### Scopes y pantalla de consentimiento
Google requiere que todos los scopes estén declarados en la pantalla de consentimiento OAuth **antes** de solicitarlos en el código. Si hay discrepancia, la autenticación falla con un error `access_denied`. La solución es asegurarse de añadir los tres scopes en Google Cloud Console antes de generar el token.

### Modo de prueba de la aplicación
Al configurar la pantalla de consentimiento como "Externo", Google pone la aplicación en **modo de prueba**. Solo los emails añadidos explícitamente como "usuarios de prueba" pueden autenticarse. Para esta práctica es suficiente, pero en producción habría que publicar la aplicación (con verificación de Google).

---

## 4. Posibles Mejoras y Extensiones

### Funcionalidad
- **`read_email(message_id)`** — Tool para leer el cuerpo completo de un email específico por su ID.
- **`search_emails(query)`** — Tool para buscar emails usando la sintaxis de búsqueda de Gmail (e.g., `from:jefe@empresa.com`).
- **`reply_email(message_id, body)`** — Tool para responder a un hilo existente manteniendo el encadenamiento correcto.
- **`mark_as_read(message_id)`** — Tool para marcar emails como leídos.
- **`list_labels`** — Resource que expone las etiquetas del usuario como `gmail://labels`.

### Seguridad y despliegue
- **Despliegue remoto con JWT:** El servidor podría exponerse como un endpoint HTTP con autenticación JWT, permitiendo que múltiples clientes MCP lo usen sin acceso directo al sistema de archivos. Esto habilitaría el punto de bonificación de la práctica.
- **Rotación automática de tokens:** Implementar un mecanismo de alerta cuando el refresh token esté próximo a expirar (Google los revoca tras 6 meses de inactividad).

### Experiencia de usuario
- **Soporte HTML:** Extender `send_email` para aceptar cuerpo en HTML usando `MIMEMultipart`.
- **Adjuntos:** Permitir adjuntar archivos usando `MIMEBase`.
- **Paginación:** Añadir soporte de cursor/paginación en `list_emails` para navegar por buzones grandes.

---

## 5. Capturas de Prueba

### Prueba 1 — Listar Emails

Prompt utilizado:
```
Lista mis últimos 5 emails
```

Tool invocada: `list_emails`

![Prueba list_emails](image/GUIA_REPLICACION/1776188859813.png)

---

### Prueba 2 — Enviar Email

Prompt utilizado:
```
Envía un email de prueba a keess.lambas@gmail.com con asunto "Test MCP" 
y cuerpo "Este es un email enviado desde mi servidor MCP"
```

Tool invocada: `send_email`

![Prueba send_email - solicitud](image/GUIA_REPLICACION/1776188922938.png)

![Prueba send_email - confirmación](image/GUIA_REPLICACION/1776188953806.png)

---

### Prueba 3 — Consultar Perfil

Prompt utilizado:
```
Obtén mi perfil de Gmail usando la herramienta get_profile
```

Tool invocada: `get_profile` (resource `gmail://profile`)

![Prueba get_profile](image/GUIA_REPLICACION/1776189104389.png)

---

### Prueba 4 — Plantilla de Redacción

Prompt utilizado:
```
Usa la herramienta redactar_email para escribir un email profesional 
a Juan García sobre la reunión del próximo lunes
```

Tool invocada: `redactar_email`

![Prueba redactar_email](image/GUIA_REPLICACION/1776189425530.png)
