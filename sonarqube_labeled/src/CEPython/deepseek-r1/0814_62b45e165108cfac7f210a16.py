def validate_as_prior_version(self, prior):
    # Check if the prior version is older than the current version
    if prior.version >= self.version:
        return False
    
    # Check all items in the prior inventory exist in the current inventory with matching attributes
    for sku in prior.items:
        if sku not in self.items:
            return False
        prior_item = prior.items[sku]
        current_item = self.items[sku]
        # Check that immutable attributes are the same
        if prior_item.name != current_item.name:
            return False
        if prior_item.description != current_item.description:
            return False
        # Additional checks for other immutable attributes can be added here
    
    return True
