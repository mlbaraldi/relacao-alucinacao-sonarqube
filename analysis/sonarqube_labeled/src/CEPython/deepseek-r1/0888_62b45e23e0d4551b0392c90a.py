def validate_version_inventories(self, version_dirs):
    """
    Each version SHOULD have an inventory up to that point.

    Also keep a record of any content digests different from those in the root inventory
    so that we can also check them when validating the content.

    version_dirs is an array of version directory names and is assumed to be in
    version sequence (1, 2, 3...).
    """
    from collections import defaultdict

    # This will store discrepancies where version digest differs from root
    self.version_digest_discrepancies = defaultdict(list)

    # Assume self.root_inventory is a dict {file_path: digest}
    root_inventory = getattr(self, 'root_inventory', {})

    for version_dir in version_dirs:
        # Check inventory exists and is valid for the version
        inventory = self.get_version_inventory(version_dir)
        if inventory is None:
            raise ValueError(f"Inventory not found or invalid for version {version_dir}")

        # Compare each entry with the root inventory
        for file_path, version_digest in inventory.items():
            root_digest = root_inventory.get(file_path)
            if root_digest is not None and version_digest != root_digest:
                self.version_digest_discrepancies[file_path].append(
                    (version_dir, version_digest, root_digest)
                )
