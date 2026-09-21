

def identify_request(request: RequestType):
    # Check if this is a Diaspora request by checking the first public message
    if request.public_messages:
        first_message = request.public_messages[0]
        if first_message.payload.get('diaspora'):
            return True

    # Check if this is a Diaspora request by checking the first private message
    if request.private_messages:
        first_message = request.private_messages[0]
        if first_message.payload.get('diaspora'):
            return True

    # Check if this is a legacy Diaspora request by checking the payload
    if request.payload.get('diaspora'):
        return True

    return False
