import os
import hashlib


def validate_version_inventories(self, version_dirs):
    root_inventory = open('root_inventory', 'r').read()
    root_content_digest = open('root_content_digest', 'r').read()

    different_content_digests = []

    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, 'inventory')
        content_digest_path = os.path.join(version_dir, 'content_digest')

        if not os.path.exists(inventory_path):
            raise Exception(f"Inventory not found for version {version_dir}")

        inventory = open(inventory_path, 'r').read()
        if inventory != root_inventory:
            raise Exception(f"Inventory mismatch for version {version_dir}")

        content_digest = open(content_digest_path, 'r').read()
        if content_digest != root_content_digest:
            different_content_digests.append((version_dir, content_digest))

    return different_content_digests
