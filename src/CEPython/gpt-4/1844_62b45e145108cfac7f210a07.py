

def validate(self, inventory, extract_spec_version=False):
    """
    Validate a given inventory.

    If extract_spec_version is True then will look at the type value to determine
    the specification version. In the case that there is no type value or it isn't
    valid, then other tests will be based on the version given in self.spec_version.
    """
    if extract_spec_version:
        # If 'type' key exists in inventory and its value is valid
        if 'type' in inventory and self.is_valid_version(inventory['type']):
            spec_version = inventory['type']
        else:
            spec_version = self.spec_version
    else:
        spec_version = self.spec_version

    # Perform other tests based on spec_version
    if not self.is_valid_inventory(inventory, spec_version):
        raise ValueError("Invalid inventory for spec version: {}".format(spec_version))

    return True
