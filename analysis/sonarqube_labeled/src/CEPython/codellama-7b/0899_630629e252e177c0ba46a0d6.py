import requests
from xrd import XRD


def retrieve_diaspora_host_meta(host):
    url = f"{host}/.well-known/host-meta"
    response = requests.get(url)
    if response.status_code == 200:
        xrd = XRD.from_xml(response.content)
        return xrd
    else:
        raise ValueError(f"Failed to retrieve host-meta document from {host}")
