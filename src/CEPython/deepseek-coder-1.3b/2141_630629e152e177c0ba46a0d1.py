import requests
import json
from typing import Optional


def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
    """
    url = f"https://{handle}/.well-known/webfinger"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return None
