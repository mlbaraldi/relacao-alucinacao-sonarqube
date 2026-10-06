import json


def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).

    :param document: The webfinger document in JSON or XRD format.
    :return: A dictionary containing the parsed information.
    """
    try:
        # Try parsing the document as JSON
        data = json.loads(document)
    except json.JSONDecodeError:
        # If the document is not in JSON format, try parsing it as XRD
        data = parse_xrd(document)

    # Extract the necessary information from the parsed data
    user_id = data["subject"]
    user_name = data["aliases"][0]
    user_image = data["links"][0]["href"]

    # Return the parsed information in a dictionary
    return {
        "user_id": user_id,
        "user_name": user_name,
        "user_image": user_image
    }
