

def register_vcs_handler(vcs, method):
    def decorator(func):
        func.vcs = vcs
        func.method = method
        return func
    return decorator
