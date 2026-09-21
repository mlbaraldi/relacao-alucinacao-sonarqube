

def identify_request(request: RequestType) -> bool:
    if request.method == "POST" and request.path == "/_matrix/client/r0/sendToDevice":
        return True
    return False
