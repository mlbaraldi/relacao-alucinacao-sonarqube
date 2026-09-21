

def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    # Check if the request has an attribute 'matrix' and it's set to True
    if hasattr(request, 'matrix') and request.matrix:
        return True
    else:
        return False
