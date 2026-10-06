def identify_request(request: RequestType):
    """
    Identify whether the request is a Diaspora request by checking for public, private, or legacy indicators.
    """
    # Check for public message
    if 'public' in request.values:
        return True
    # Check for private message
    if 'encrypted' in request.values:
        return True
    # Check for legacy payload
    if 'legacy' in request.values:
        return True
    return False
