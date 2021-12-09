import base64
from typing import Optional

import requests


def _get_bearer(client_id: str, client_secret: str) -> str:
    encoded_bearer_info = (client_id + ":" + client_secret).encode()
    encoded_bearer_info = base64.b64encode(encoded_bearer_info)
    encoded_bearer_info = encoded_bearer_info.decode("utf-8")
    return encoded_bearer_info


def _request_api(url: str, method_name: str, bearer_info: str, **kwargs) -> requests.Response:
    headers = {
        "Authorization": f"Basic {bearer_info}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    request_method = getattr(requests, method_name)
    return request_method(url, headers=headers, **kwargs)


def get_access_token(client_id: str, client_secret: str) -> Optional[str]:
    """Retrieves access token for the provided client id & secret"""
    url = "https://accounts.spotify.com/api/token"
    bearer_info = _get_bearer(client_id, client_secret)
    payload = {"grant_type": "client_credentials"}

    request_result = _request_api(
        url=url,
        method_name="post",
        bearer_info=bearer_info,
        **dict(data=payload),
    )

    if request_result.ok:
        return request_result.json()["access_token"]
    return None
