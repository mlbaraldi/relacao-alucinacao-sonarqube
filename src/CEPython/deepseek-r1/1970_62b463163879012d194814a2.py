def add_asset(self, basename, file_path):
    import os
    filename = os.path.basename(file_path)
    root, ext = os.path.splitext(filename)
    if root != basename:
        raise ValueError(f"Filename '{filename}' does not match the provided basename '{basename}'")
    self.assets[filename] = file_path
