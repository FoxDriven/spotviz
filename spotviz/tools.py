import base64

import requests


def get_access_token(client_id: str, client_secret: str) -> str:
    """Retrieves access token for the provided client id & secret"""
    url = "https://accounts.spotify.com/api/token"

    encoded_auth = (client_id + ":" + client_secret).encode()
    encoded_auth = base64.b64encode(encoded_auth)
    encoded_auth = encoded_auth.decode("utf-8")

    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {
        "grant_type": "client_credentials",
    }

    request_result = requests.post(url, headers=headers, data=payload)

    if request_result.ok:
        return request_result.json()["access_token"]
    return None
