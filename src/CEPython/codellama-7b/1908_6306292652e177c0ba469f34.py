import requests


def fetch_content_type(url: str) -> Optional[str]:
    try:
        response = requests.head(url)
        content_type = response.headers.get('Content-Type')
        return content_type
    except requests.exceptions.RequestException:
        return None
