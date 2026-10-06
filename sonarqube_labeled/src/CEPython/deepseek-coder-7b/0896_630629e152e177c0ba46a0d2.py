import requests
import json


def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    # Construct the webfinger URL
    webfinger_url = f"https://{handle}.pod.in/{handle}.json"

    try:
        # Send a GET request to the webfinger URL
        response = requests.get(webfinger_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Example usage:
# data = retrieve_and_parse_diaspora_webfinger("example_handle")
# if data:
#     print(json.dumps(data, indent=4))
