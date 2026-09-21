

def validate_as_prior_version(self, prior):
    if not isinstance(prior, InventoryValidator):
        return False
    return prior.version < self.version.version
