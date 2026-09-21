def retrieve_diaspora_host_meta(host):
    import requests
    """
    Retrieve a remote Diaspora host-meta document.

    :arg host: Host to retrieve from
    :returns: ``XRD`` instance
    """
    url = f"https://{host}/.well-known/host-meta"
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return XRD.parse(response.text)
