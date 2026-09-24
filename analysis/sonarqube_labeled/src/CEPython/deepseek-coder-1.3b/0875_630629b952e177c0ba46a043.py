import requests
import json


def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Generate a NodeInfo .well-known document.

    See spec: http://nodeinfo.diaspora.software

    :arg url: The full base url with protocol, ie https://example.com
    :arg document_path: Custom NodeInfo document path if supplied (optional)
    :returns: dict
    """

    # If document_path is provided, construct the full URL
    if document_path:
        url = url + '/' + document_path

    # Send a GET request to the URL
    response = requests.get(url)

    # If the GET request is successful, parse the JSON response
    if response.status_code == 200:
        return response.json()
    else:
        return None
