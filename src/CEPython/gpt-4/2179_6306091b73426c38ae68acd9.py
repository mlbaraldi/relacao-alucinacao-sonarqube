

def workspace_manager(cls):
    """
    Gets the workspace manager.
    """
    try:
        return cls.workspace_manager
    except AttributeError:
        raise Exception("The class does not have a workspace manager.")
