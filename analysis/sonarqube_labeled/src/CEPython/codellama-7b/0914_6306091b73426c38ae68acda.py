

def plugins_manager(cls):
    # Get the plugin manager from the class
    plugin_manager = cls.plugin_manager

    # Check if the plugin manager is None
    if plugin_manager is None:
        # If the plugin manager is None, create a new one
        plugin_manager = PluginManager()
        cls.plugin_manager = plugin_manager

    # Return the plugin manager
    return plugin_manager
