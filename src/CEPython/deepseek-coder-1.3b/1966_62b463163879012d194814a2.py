

def add_asset(self, basename, file_path):
    """
    Add an asset to the dictionary.

    Args:
        basename (str): The base name of the asset.
        file_path (str): The file path of the asset.

    Returns:
        None
    """
    # Create a dictionary if it doesn't exist
    if not hasattr(self, 'assets'):
        self.assets = {}

    # Add the asset to the dictionary
    self.assets[basename] = file_path
