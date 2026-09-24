import requests


def get_nodeinfo_well_known_document(url, document_path=None):
    if document_path is None:
        document_path = f"{url}/.well-known/nodeinfo"

    response = requests.get(document_path)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Failed to retrieve NodeInfo document from {document_path}")
