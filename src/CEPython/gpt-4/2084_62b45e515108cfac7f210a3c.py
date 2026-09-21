import os


def initialize(self):
    """
    Create and initialize a new OCFL storage root.
    """
    if not os.path.exists(self.root_path):
        os.makedirs(self.root_path)
        print(f"OCFL storage root created at {self.root_path}")
    else:
        print(f"OCFL storage root already exists at {self.root_path}")
