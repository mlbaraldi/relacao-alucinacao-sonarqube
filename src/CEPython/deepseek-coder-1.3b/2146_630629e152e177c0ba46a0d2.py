import requests
import json


def retrieve_and_parse_diaspora_webfinger(handle):
    # Construct the URL for the webfinger document
    url = f"https://{handle}.diaspora.net/.well-known/webfinger"

    # Make the HTTP request
    response = requests.get(url)

    # Parse the JSON response
    data = json.loads(response.text)

    # Return the parsed data
    return data
