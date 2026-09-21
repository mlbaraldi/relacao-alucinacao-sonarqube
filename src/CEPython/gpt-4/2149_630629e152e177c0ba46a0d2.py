import requests


def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    # Construct the URL
    url = f"https://diaspora.example.com/.well-known/webfinger?resource=acct:{handle}"

    # Send a GET request to the URL
    response = requests.get(url)

    # If the request was successful, parse the JSON response into a Python dictionary
    if response.status_code == 200:
        return response.json()
    else:
        return None
