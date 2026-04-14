import os
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP

# Permisos que solicita la aplicación
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify"
]

mcp = FastMCP("Gmail MCP Server")

# Ruta al directorio donde están credentials.json y token.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")


def get_gmail_service():
    """Autentica con OAuth y devuelve el servicio de Gmail."""
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


# ---------------------------------------------------------------------------
# TOOLS
# ---------------------------------------------------------------------------

@mcp.tool()
def list_emails(max_results: int = 10) -> str:
    """Lista los emails más recientes de la bandeja de entrada.

    Args:
        max_results: Número máximo de emails a listar (por defecto 10)
    """
    service = get_gmail_service()
    results = service.users().messages().list(
        userId="me",
        maxResults=max_results,
        labelIds=["INBOX"]
    ).execute()

    messages = results.get("messages", [])
    if not messages:
        return "No se encontraron emails."

    emails = []
    for msg in messages:
        message = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="metadata",
            metadataHeaders=["From", "Subject", "Date"]
        ).execute()

        headers = {h["name"]: h["value"] for h in message["payload"]["headers"]}
        emails.append(
            f"ID: {msg['id']}\n"
            f"De: {headers.get('From', 'Desconocido')}\n"
            f"Asunto: {headers.get('Subject', 'Sin asunto')}\n"
            f"Fecha: {headers.get('Date', 'Sin fecha')}\n"
        )

    return "\n---\n".join(emails)


@mcp.tool()
def send_email(to: str, subject: str, body: str) -> str:
    """Envía un email a través de Gmail.

    Args:
        to: Dirección de email del destinatario
        subject: Asunto del email
        body: Cuerpo del email en texto plano
    """
    service = get_gmail_service()

    message = MIMEText(body)
    message["to"] = to
    message["subject"] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    send_message = service.users().messages().send(
        userId="me",
        body={"raw": raw}
    ).execute()

    return f"Email enviado correctamente. ID: {send_message['id']}"


# ---------------------------------------------------------------------------
# RESOURCES
# ---------------------------------------------------------------------------

@mcp.resource("gmail://profile")
def get_profile_resource() -> str:
    """Recurso MCP: perfil del usuario de Gmail en gmail://profile."""
    service = get_gmail_service()
    profile = service.users().getProfile(userId="me").execute()

    return (
        f"Email: {profile.get('emailAddress', 'No disponible')}\n"
        f"Total de mensajes: {profile.get('messagesTotal', 0)}\n"
        f"Hilos totales: {profile.get('threadsTotal', 0)}"
    )


# ---------------------------------------------------------------------------
# TOOLS (adicional para facilitar acceso al perfil)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_profile() -> str:
    """Obtiene el perfil del usuario autenticado en Gmail: email, total de mensajes y hilos."""
    service = get_gmail_service()
    profile = service.users().getProfile(userId="me").execute()

    return (
        f"Email: {profile.get('emailAddress', 'No disponible')}\n"
        f"Total de mensajes: {profile.get('messagesTotal', 0)}\n"
        f"Hilos totales: {profile.get('threadsTotal', 0)}"
    )


# ---------------------------------------------------------------------------
# PROMPTS
# ---------------------------------------------------------------------------

@mcp.prompt()
def redactar_email_prompt(destinatario: str, tema: str, tono: str = "profesional") -> str:
    """Prompt MCP: plantilla para redactar un email."""
    return f"""Redacta un email con las siguientes características:
- Destinatario: {destinatario}
- Tema: {tema}
- Tono: {tono}

El email debe ser claro, conciso y apropiado para el tono indicado.
Incluye un saludo, el cuerpo del mensaje y una despedida adecuada."""


# ---------------------------------------------------------------------------
# TOOLS (adicional para facilitar acceso al prompt de redacción)
# ---------------------------------------------------------------------------

@mcp.tool()
def redactar_email(destinatario: str, tema: str, tono: str = "profesional") -> str:
    """Genera un borrador de email usando la plantilla de redacción.

    Args:
        destinatario: Nombre o dirección del destinatario
        tema: Tema o propósito del email
        tono: Tono del email (profesional, informal, formal)
    """
    return f"""Redacta un email con las siguientes características:
- Destinatario: {destinatario}
- Tema: {tema}
- Tono: {tono}

El email debe ser claro, conciso y apropiado para el tono indicado.
Incluye un saludo, el cuerpo del mensaje y una despedida adecuada."""


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()
