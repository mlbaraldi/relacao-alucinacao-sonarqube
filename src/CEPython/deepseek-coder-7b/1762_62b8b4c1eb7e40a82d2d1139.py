

def verifyClass(iface, candidate, tentative=False):
    """
    Verify that the *candidate* might correctly provide *iface*.
    """
    iface_methods = iface.__dict__.keys()
    candidate_methods = candidate.__dict__.keys()
    
    if not all(method in candidate_methods for method in iface_methods):
        return False
    
    if not tentative:
        for method in iface_methods:
            if not callable(getattr(candidate, method)):
                return False
    
    return True
