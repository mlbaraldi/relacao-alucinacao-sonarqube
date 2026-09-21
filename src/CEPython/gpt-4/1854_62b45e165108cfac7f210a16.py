

def validate_as_prior_version(self, prior):
    """
    Check that prior is a valid prior version of the current inventory object.
    The input variable prior is also expected to be an InventoryValidator object
    and both self and prior inventories are assumed to have been checked for
    internal consistency.
    """
    if not isinstance(prior, InventoryValidator):
        raise ValueError("Input must be an instance of InventoryValidator")

    if prior.version >= self.version:
        return False
    return True
