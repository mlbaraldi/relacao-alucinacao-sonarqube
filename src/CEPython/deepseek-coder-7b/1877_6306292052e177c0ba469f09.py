from typing import Any


def identify_request(request: RequestType):
    """
    Try to identify whether this is a Diaspora request.
    Try first public message. Then private message. The check if this is a legacy payload.
    """
    if request.public_message:
        return "This is a Diaspora public message request."
    elif request.private_message:
        return "This is a Diaspora private message request."
    elif request.is_legacy():
        return "This is a Diaspora legacy payload request."
    else:
        return "This is not a recognized Diaspora request."

# Example usage:
