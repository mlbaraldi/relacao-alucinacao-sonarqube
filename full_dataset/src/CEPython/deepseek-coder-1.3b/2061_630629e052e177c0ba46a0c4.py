import json
from typing import Dict


def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).
    """
    # Check if the document is in JSON format
    try:
        data = json.loads(document)
    except json.JSONDecodeError:
        # If not, try to parse it as XRD
        # This is a placeholder, as the actual parsing would depend on the specifics of the Diaspora webfinger specification
        data = {"profile": document}

    return data
