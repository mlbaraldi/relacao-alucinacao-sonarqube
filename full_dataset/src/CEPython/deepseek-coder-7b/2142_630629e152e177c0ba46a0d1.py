import requests
from typing import Optional


def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
    """
    # Extract the domain from the handle
    domain = handle.split('@')[-1] if '@' in handle else None
    
    if domain:
        # Construct the webfinger URL
        webfinger_url = f'https://{domain}/.well-known/webfinger?resource={handle}'
        
        try:
            # Make the GET request
            response = requests.get(webfinger_url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Return the content of the response
                return response.text
            else:
                # If the request was not successful, return None
                return None
        except requests.RequestException:
            # If there was an exception during the request, return None
            return None
    else:
        # If the handle does not contain a domain, return None
        return None

# Example usage:
