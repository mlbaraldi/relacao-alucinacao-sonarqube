import requests
import xml.etree.ElementTree as ET


def retrieve_and_parse_diaspora_webfinger(handle):
    # Retrieve the webfinger document
    response = requests.get(f"https://{handle}.diaspora.software/.well-known/webfinger?resource={handle}")
    if response.status_code != 200:
        raise ValueError(f"Failed to retrieve webfinger document for handle {handle}")

    # Parse the webfinger document
    root = ET.fromstring(response.content)
    links = root.findall(".//{http://www.w3.org/2005/Atom}link")
    return {link.attrib["rel"]: link.attrib["href"] for link in links}
