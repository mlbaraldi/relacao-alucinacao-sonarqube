def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    """
    Ensure that sender and entity handles match.

    Verifies that the sender_handle (from headers) matches the entity_handle (from payload content).
    Returns True if they match, False otherwise.
    """
    return sender_handle == entity_handle
