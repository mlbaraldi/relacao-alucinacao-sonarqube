def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    import requests
    from urllib.parse import urlencode
    from typing import Optional
    """
    Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
    """
    try:
        # Process the handle into a resource identifier
        if handle.startswith('acct:'):
            resource = handle
        else:
            resource = f'acct:{handle}'
        
        # Extract the domain part from the resource
        account_part = resource[5:]  # Remove 'acct:' prefix
        if '@' not in account_part:
            return None
        _, domain = account_part.split('@', 1)  # Split into local part and domain
        
        # Construct the webfinger URL
        query = urlencode({'resource': resource})
        url = f'https://{domain}/.well-known/webfinger?{query}'
        
        # Make the GET request with appropriate headers and timeout
        headers = {'Accept': 'application/jrd+json'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        
        return response.text
    except Exception:
        return None
