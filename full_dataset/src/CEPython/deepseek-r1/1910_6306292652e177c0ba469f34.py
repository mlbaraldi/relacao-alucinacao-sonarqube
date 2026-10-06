def fetch_content_type(url: str) -> Optional[str]:
    import requests
    from typing import Optional
    """
    Fetch the HEAD of the remote url to determine the content type.
    """
    try:
        response = requests.head(url, timeout=5)
        return response.headers.get('Content-Type')
    except requests.exceptions.RequestException:
        return None
