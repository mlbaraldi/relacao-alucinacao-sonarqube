

def validate_version_inventories(self, version_dirs):
    # Keep track of the root inventory and its content digests
    root_inventory = self.get_root_inventory()
    root_digests = {
        digest: True
        for digest in root_inventory.get_content_digests()
    }

    # Iterate over the version directories
    for version_dir in version_dirs:
        # Get the inventory for the current version
        inventory = self.get_inventory(version_dir)

        # Check that the inventory is not empty
        if inventory.is_empty():
            raise ValueError("Inventory is empty")

        # Check that the inventory has the same content digests as the root inventory
        for digest in inventory.get_content_digests():
            if digest not in root_digests:
                raise ValueError("Inventory has unknown content digest")

        # Keep track of the content digests for the current version
        version_digests = {
            digest: True
            for digest in inventory.get_content_digests()
        }

        # Check that the content digests for the current version are different from the root inventory
        for digest in version_digests:
            if digest in root_digests:
                raise ValueError("Inventory has duplicate content digest")

    # Return the list of content digests for the current version
    return version_digests
