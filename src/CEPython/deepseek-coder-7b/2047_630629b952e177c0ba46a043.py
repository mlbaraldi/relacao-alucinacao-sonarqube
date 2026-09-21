import requests


def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Generate a NodeInfo .well-known document.

    See spec: http://nodeinfo.diaspora.software

    :arg url: The full base url with protocol, ie https://example.com
    :arg document_path: Custom NodeInfo document path if supplied (optional)
    :returns: dict or None if the document is not found or cannot be fetched
    """
    # Construct the URL for the NodeInfo document
    if document_path:
        nodeinfo_url = f"{url}/{document_path}"
    else:
        nodeinfo_url = f"{url}/.well-known/nodeinfo"

    try:
        # Send a GET request to fetch the NodeInfo document
        response = requests.get(nodeinfo_url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            nodeinfo_data = response.json()
            return nodeinfo_data
        else:
            print(f"Failed to fetch NodeInfo document: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Example usage:
# nodeinfo = get_nodeinfo_well_known_document('https://example.com')
# print(nodeinfo)
