import base64
from typing import Optional

import requests


def _get_bearer(client_id: str, client_secret: str) -> str:
    encoded_bearer_info = (client_id + ":" + client_secret).encode()
    encoded_bearer_info = base64.b64encode(encoded_bearer_info)
    encoded_bearer_info = encoded_bearer_info.decode("utf-8")
    return encoded_bearer_info


def get_access_token(client_id: str, client_secret: str) -> Optional[str]:
    """Retrieves access token for the provided client id & secret"""
    url = "https://accounts.spotify.com/api/token"
    bearer_token = _get_bearer(client_id, client_secret)
    headers = {
        "Authorization": f"Basic {bearer_token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {"grant_type": "client_credentials"}

    request_result = requests.post(
        url=url,
        headers=headers,
        data=payload,
    )

    if request_result.ok:
        return request_result.json()["access_token"]
    return None


def get_playlist_info(playlist_id: str, bearer_token: str):
    """Retrieve playlist info for the provided id and token"""
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    request_result = requests.get(url, headers=headers)

    return request_result
