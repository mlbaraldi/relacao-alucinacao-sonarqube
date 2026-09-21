

def workspace_manager(cls):
    # Get the workspace manager from the current thread
    workspace_manager = cls.get_workspace_manager()

    # If the workspace manager is not set, create a new one
    if workspace_manager is None:
        workspace_manager = cls.create_workspace_manager()

    return workspace_manager
