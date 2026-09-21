from typing import Type


def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    if request.matrix_id:
        return True
    else:
        return False
