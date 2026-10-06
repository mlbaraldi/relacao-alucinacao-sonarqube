import requests
from typing import Optional


def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
    """
    try:
        # Construct the URL for the webfinger document
        url = f"https://{handle}/.well-known/webfinger"

        # Make a GET request to the URL
        response = requests.get(url)

        # If the request was successful, return the text of the response
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        # If any error occurred, return None
        return None
