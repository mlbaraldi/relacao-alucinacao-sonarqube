

def identify_request(request: RequestType):
    """
    Try to identify whether this is a Diaspora request.

    Try first public message. Then private message. Then check if this is a legacy payload.
    """
    if is_diaspora_request(request):
        return "Diaspora request"
    elif is_public_message(request):
        return "Public message"
    elif is_private_message(request):
        return "Private message"
    elif is_legacy_payload(request):
        return "Legacy payload"
    else:
        return "Unknown request"
