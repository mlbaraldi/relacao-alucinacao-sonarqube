import json
from typing import Dict


def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).
    """
    try:
        # Attempt to parse the document as JSON
        return json.loads(document)
    except json.JSONDecodeError:
        # If JSON parsing fails, assume it's XRD and try to parse it accordingly
        # This is a placeholder for XRD parsing logic, which is not provided in the question
        raise NotImplementedError("XRD parsing logic is not implemented.")

# Example usage:
