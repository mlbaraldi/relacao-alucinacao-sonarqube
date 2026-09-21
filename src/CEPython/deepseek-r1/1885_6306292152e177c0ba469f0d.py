def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    return request.path.startswith('/_matrix/')
