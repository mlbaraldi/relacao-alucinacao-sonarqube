import os


def initialize(self):
    """
    Create and initialize a new OCFL storage root.
    """
    if not os.path.exists(self.path):
        os.makedirs(self.path)
    else:
        print(f"The directory {self.path} already exists.")
