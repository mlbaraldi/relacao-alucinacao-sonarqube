

def register_vcs_handler(vcs, method):
    """
    Create decorator to mark a method as the handler of a VCS.
    """
    
    # Define a new decorator
    def decorator(func):
        # Store the method in the VCS's handler list
        vcs.register_handler(method, func)
        
        # Return the original function
        return func
    
    # Return the new decorator
    return decorator
