import requests
from typing import Optional


def fetch_content_type(url: str) -> Optional[str]:
    """
    Fetch the HEAD of the remote url to determine the content type.
    """
    try:
        response = requests.head(url)
        content_type = response.headers.get('content-type')
        return content_type
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
