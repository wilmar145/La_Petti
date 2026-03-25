# app/auth/auth0_service.py
import httpx

AUTH0_DOMAIN = "tu-dominio.auth0.com"
AUTH0_CLIENT_ID = "tu_client_id"
AUTH0_CLIENT_SECRET = "tu_client_secret"

async def actualizar_metadata_usuario(user_id: str, tipo_doc: str, num_doc: str, token: str):
    """
    Cumple con el punto 3.0: Formulario posterior que guarda info en metadata.
    """
    url = f"https://{AUTH0_DOMAIN}/api/v2/users/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "user_metadata": {
            "tipo_documento": tipo_doc,
            "numero_documento": num_doc
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.patch(url, json=payload, headers=headers)
        return response.json()
