

def add_asset(self, basename, file_path):
    """
    Add an asset to the asset dictionary.

    :param asset_dict: The dictionary to add the asset to.
    :param basename: The base name of the asset.
    :param file_path: The file path of the asset.
    """
    asset_dict[basename] = file_path
    return asset_dict
