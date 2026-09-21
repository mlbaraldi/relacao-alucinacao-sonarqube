def get_nodeinfo_well_known_document(url, document_path=None):
    from urllib.parse import urljoin
    """
    Generate a NodeInfo .well-known document.

    See spec: http://nodeinfo.diaspora.software

    :arg url: The full base url with protocol, ie https://example.com
    :arg document_path: Custom NodeInfo document path if supplied (optional)
    :returns: dict
    """
    document_path = document_path if document_path is not None else 'nodeinfo'
    versions = ['2.0', '2.1']
    links = []
    for version in versions:
        path = f"{document_path}/{version}"
        href = urljoin(url, path)
        rel = f"http://nodeinfo.diaspora.software/ns/schema/{version}"
        links.append({'rel': rel, 'href': href})
    return {'links': links}
