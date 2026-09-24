def discard(self, n=-1, qid=-1, dehydration_hooks=None,
                hydration_hooks=None, **handlers):
    """
    Appends a DISCARD message to the output queue.

    :param n: number of records to discard, default = -1 (ALL)
    :param qid: query ID to discard for, default = -1 (last query)
    :param dehydration_hooks: Hooks to dehydrate custom types for the response
    :param hydration_hooks: Hooks to hydrate types from the response data
    :param handlers: Handler functions for the response (e.g., on_success, on_failure)
    :return: A Response object configured with the provided hooks and handlers
    """
    # Append the DISCARD message to the output queue
    self.output_queue.append(("DISCARD", {"n": n, "qid": qid}))
    # Create and return the Response object with the specified hooks and handlers
    return Response(
        dehydration_hooks=dehydration_hooks,
        hydration_hooks=hydration_hooks,
        **handlers
    )
