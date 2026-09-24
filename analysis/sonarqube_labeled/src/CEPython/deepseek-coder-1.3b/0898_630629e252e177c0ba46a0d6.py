import requests


def retrieve_diaspora_host_meta(host):
    """
    Retrieve a remote Diaspora host-meta document.

    :arg host: Host to retrieve from
    :returns: ``XRD`` instance
    """

    # Define the URL for the Diaspora API
    url = f"https://{host}/host-meta"

    # Send a GET request to the Diaspora API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # If successful, return the response
        return response.json()
    else:
        # If not successful, raise an exception
        raise Exception(f"Failed to retrieve host-meta document from {host}")
