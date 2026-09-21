

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Generate a NodeInfo .well-known document.

    See spec: http://nodeinfo.diaspora.software

    :arg url: The full base url with protocol, ie https://example.com
    :arg document_path: Custom NodeInfo document path if supplied (optional)
    :returns: dict
    """
    # If no custom document path is supplied, use the default one
    if document_path is None:
        document_path = "/.well-known/nodeinfo"

    # Create the NodeInfo document
    nodeinfo_document = {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": url + document_path
            }
        ]
    }

    return nodeinfo_document
