

def identify_request(request: RequestType):
    """
    Try to identify whether this is a Diaspora request.

    Try first public message. Then private message. The check if this is a legacy payload.
    """

    # Try first public message
    if request.public_message:
        return "Public message"

    # If public message fails, try private message
    elif request.private_message:
        return "Private message"

    # If both public and private messages fail, it's a legacy payload
    else:
        return "Legacy payload"
