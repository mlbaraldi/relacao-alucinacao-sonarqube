import json
import xmltodict
from typing import Dict


def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).

    https://diaspora.github.io/diaspora_federation/discovery/webfinger.html
    """
    if document.strip().startswith('<'):
        # XRD format
        return xmltodict.parse(document)
    else:
        # JSON format
        return json.loads(document)
