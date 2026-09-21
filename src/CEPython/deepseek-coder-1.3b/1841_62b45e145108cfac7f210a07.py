

def validate(self, inventory, extract_spec_version=False):
    """
    Validate a given inventory.

    If extract_spec_version is True then will look at the type value to determine
    the specification version. In the case that there is no type value or it isn't
    valid, then other tests will be based on the version given in self.spec_version.
    """

    # Check if inventory is a dictionary
    if not isinstance(inventory, dict):
        raise ValueError("Inventory must be a dictionary")

    # Check if inventory has a 'type' key
    if 'type' not in inventory:
        raise ValueError("Inventory must have a 'type' key")

    # Check if 'type' key has a valid value
    type_value = inventory['type']
    if not isinstance(type_value, str):
        raise ValueError("The 'type' key must have a string value")

    # Check if 'version' key exists
    if 'version' not in inventory:
        raise ValueError("Inventory must have a 'version' key")

    # Check if 'version' key has a valid value
    version_value = inventory['version']
    if not isinstance(version_value, str):
        raise ValueError("The 'version' key must have a string value")

    # Check if 'spec_version' attribute exists
    if not hasattr(self, 'spec_version'):
        raise ValueError("The class must have a 'spec_version' attribute")

    # Check if 'spec_version' attribute has a valid value
    if not isinstance(self.spec_version, str):
        raise ValueError("The 'spec_version' attribute must have a string value")

    # If extract_spec_version is True, check if 'spec_version' is the same as the 'version'
    if extract_spec_version and self.spec_version != version_value:
