def workspace_manager(cls):
    """
    Gets the workspace manager.
    """
    workspace_manager_instance = cls()
    @classmethod
    def get_workspace_manager(cls):
        return workspace_manager_instance
    cls.get_workspace_manager = get_workspace_manager
    return cls
