def retrieve_and_parse_diaspora_webfinger(handle):
    import requests
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    # Split the handle into local part and domain
    local_part, domain = handle.split('@', 1)
    
    # Construct the WebFinger URL
    url = f"https://{domain}/.well-known/webfinger"
    params = {'resource': f'acct:{handle}'}
    headers = {'Accept': 'application/jrd+json, application/json'}
    
    # Send the GET request
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()  # Raise exception for HTTP errors
    
    # Parse and return the JSON response
    return response.json()
