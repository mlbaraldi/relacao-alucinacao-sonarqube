def initialize(self):
    import os
    import json
    """
    Create and initialize a new OCFL storage root.
    """
    # Create the root directory if it doesn't exist
    os.makedirs(self.root_path, exist_ok=True)

    # Check for existing OCFL files
    version_file = os.path.join(self.root_path, '0=ocfl_1.1')
    layout_file = os.path.join(self.root_path, 'ocfl_layout.json')

    if os.path.exists(version_file) or os.path.exists(layout_file):
        raise ValueError("OCFL storage root is already initialized.")

    # Check if the directory is empty
    if os.listdir(self.root_path):
        raise ValueError("Cannot initialize OCFL root in a non-empty directory.")

    # Create the version declaration file
    with open(version_file, 'w') as f:
        f.write("ocfl_1.1\n")

    # Create the layout configuration file
    layout = {
        "type": "https://ocfl.io/1.1/spec/#hierarchy-hashed"
    }
    with open(layout_file, 'w') as f:
        json.dump(layout, f, indent=2)
