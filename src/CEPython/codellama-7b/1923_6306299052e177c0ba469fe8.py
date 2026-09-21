

def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    if sender_handle != entity_handle:
        raise ValueError("Sender and entity handles do not match")
