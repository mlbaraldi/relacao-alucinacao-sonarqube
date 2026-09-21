

def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None,
              db=None, imp_user=None, dehydration_hooks=None,
              hydration_hooks=None, **handlers):
    # Create a new transaction object
    transaction = Transaction(mode, bookmarks, metadata, timeout, db, imp_user,
                              dehydration_hooks, hydration_hooks)

    # Add the transaction to the output queue
    self.output_queue.append(transaction)

    # Return a Response object with the transaction and any handlers
    return Response(transaction, handlers)
