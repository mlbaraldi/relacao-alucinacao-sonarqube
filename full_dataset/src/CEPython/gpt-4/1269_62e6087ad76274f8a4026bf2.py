

def discard(self, n=-1, qid=-1, dehydration_hooks=None,
                hydration_hooks=None, **handlers):
    # Create a DISCARD message
    message = {
        'action': 'DISCARD',
        'n': n,
        'qid': qid,
    }

    # If dehydration_hooks is provided, add it to the message
    if dehydration_hooks is not None:
        message['dehydration_hooks'] = dehydration_hooks

    # If hydration_hooks is provided, add it to the message
    if hydration_hooks is not None:
        message['hydration_hooks'] = hydration_hooks

    # Append the message to the output queue
    self.output_queue.append(message)

    # Create a Response object with the provided handlers
    response = Response(**handlers)

    return response
