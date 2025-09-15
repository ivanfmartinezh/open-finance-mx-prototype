from __future__ import annotations

import os

from belvo.client import Client  # type: ignore
from dotenv import load_dotenv

load_dotenv()


def get_belvo_client() -> Client:
    """Crea y retorna un cliente de Belvo usando variables de entorno." """
    secret_id = os.getenv("BELVO_ID")
    secret_password = os.getenv("BELVO_PASSWORD")
    base_url = os.getenv("BELVO_BASE_URL", "https://sandbox.belvo.com")

    if not secret_id or not secret_password:
        raise RuntimeError("Faltan BELVO_ID o BELVO_PASSWORD " "en el entorno (.env)")

    return Client(secret_id, secret_password, base_url)
