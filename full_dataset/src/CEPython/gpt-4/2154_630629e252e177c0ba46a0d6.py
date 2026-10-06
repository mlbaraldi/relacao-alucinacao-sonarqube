import requests
from lxml import objectify


def retrieve_diaspora_host_meta(host):
    """
    Retrieve a remote Diaspora host-meta document.

    :arg host: Host to retrieve from
    :returns: ``XRD`` instance
    """
    url = f"https://{host}/.well-known/host-meta"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception if the request failed

    # Parse the XML response into an XRD instance
    xrd = objectify.fromstring(response.content)

    return xrd
