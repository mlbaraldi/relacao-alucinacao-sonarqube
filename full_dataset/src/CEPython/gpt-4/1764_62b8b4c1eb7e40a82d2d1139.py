

def verifyClass(iface, candidate, tentative=False):
    """
    Verify that the *candidate* might correctly provide *iface*.
    """
    for attr in dir(iface):
        if not hasattr(candidate, attr):
            if tentative:
                return False
            else:
                raise TypeError(f"{candidate.__name__} does not implement {attr} from {iface.__name__}")
    return True
