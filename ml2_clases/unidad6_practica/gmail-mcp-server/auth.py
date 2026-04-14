"""
Ejecuta este script UNA VEZ para generar token.json.
Abrirá el navegador para que autorices el acceso a Gmail.
"""
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify"
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")

print("Abriendo navegador para autorizar acceso a Gmail...")
flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
creds = flow.run_local_server(port=0)

with open(TOKEN_FILE, "w") as token:
    token.write(creds.to_json())

print(f"token.json generado correctamente en: {TOKEN_FILE}")
