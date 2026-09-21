import requests
from typing import Optional


def fetch_content_type(url: str) -> Optional[str]:
    """
    Fetch the HEAD of the remote url to determine the content type.
    """
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return response.headers['Content-Type']
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None
