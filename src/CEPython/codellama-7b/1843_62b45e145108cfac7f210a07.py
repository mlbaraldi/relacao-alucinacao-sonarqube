

def validate(self, inventory, extract_spec_version=False):
    # Check if the inventory is a dictionary
    if not isinstance(inventory, dict):
        raise ValueError("Inventory must be a dictionary")

    # Check if the inventory has a 'type' key
    if 'type' not in inventory:
        raise ValueError("Inventory must have a 'type' key")

    # Check if the 'type' value is valid
    if inventory['type'] not in ['spec_version', 'inventory']:
        raise ValueError("Invalid 'type' value")

    # Check if the inventory has a 'version' key
    if 'version' not in inventory:
        raise ValueError("Inventory must have a 'version' key")

    # Check if the 'version' value is valid
    if inventory['version'] not in ['1.0', '2.0']:
        raise ValueError("Invalid 'version' value")

    # Check if the inventory has a 'spec_version' key
    if 'spec_version' not in inventory:
        raise ValueError("Inventory must have a 'spec_version' key")

    # Check if the 'spec_version' value is valid
    if inventory['spec_version'] not in ['1.0', '2.0']:
        raise ValueError("Invalid 'spec_version' value")

    # Check if the inventory has a 'inventory' key
    if 'inventory' not in inventory:
        raise ValueError("Inventory must have an 'inventory' key")

    # Check if the 'inventory' value is a list
    if not isinstance(inventory['inventory'], list):
        raise ValueError("Inventory must have a list of items")

    # Check if the 'inventory' list is not empty
    if len(inventory['inventory']) == 0:
        raise ValueError("Inventory must have at least one item")

    # Check if the 'inventory' list contains only valid items
