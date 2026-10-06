

def plugins_manager(cls):
    """
    Gets the plugin manager.
    """
    try:
        return cls.plugin_manager
    except AttributeError:
        print("The class does not have a plugin manager.")
        return None
