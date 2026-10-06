

def add_asset(self, basename, file_path):
    """
    Add a new asset to the assets dictionary.
    The basename is the key and the file_path is the value.
    """
    self.assets[basename] = file_path
