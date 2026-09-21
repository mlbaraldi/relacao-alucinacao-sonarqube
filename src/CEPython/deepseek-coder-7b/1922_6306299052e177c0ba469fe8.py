

def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    """
    Ensure that sender and entity handles match.
    """
    if sender_handle == entity_handle:
        return True
    else:
        return False
