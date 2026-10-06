import os


def validate_version_inventories(self, version_dirs):
    for version in version_dirs:
        inventory_path = os.path.join(version, 'inventory.txt')
        if not os.path.exists(inventory_path):
            print(f'Inventory for version {version} does not exist.')
            return False

        with open(inventory_path, 'r') as inventory_file:
            version_digests = inventory_file.readlines()

        with open(self.root_inventory, 'r') as root_inventory_file:
            root_digests = root_inventory_file.readlines()

        for digest in version_digests:
            if digest not in root_digests:
                self.diff_digests.append(digest)

    if self.diff_digests:
        print('Content digests different from those in the root inventory:')
        for digest in self.diff_digests:
            print(digest)
        return False

    return True
