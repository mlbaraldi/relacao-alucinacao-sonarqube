import ocf


def initialize(self):
    """
    Create and initialize a new OCFL storage root.
    """
    # Create a new storage root
    storage_root = ocf.StorageRoot()

    # Initialize the storage root
    storage_root.initialize()

    # Return the storage root
    return storage_root
