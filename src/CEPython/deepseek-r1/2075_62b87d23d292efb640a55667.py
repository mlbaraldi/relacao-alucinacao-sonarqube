def register_vcs_handler(vcs, method):
    """
    Create decorator to mark a method as the handler of a VCS.
    """
    def decorator(method):
        setattr(method, '_vcs_handler', vcs)
        return method
    return decorator
