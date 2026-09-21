

def verifyClass(iface, candidate, tentative=False):
    if not isinstance(candidate, type):
        raise TypeError("Candidate must be a class")
    if not issubclass(candidate, iface):
        raise TypeError("Candidate does not implement the interface")
    if tentative:
        return True
    else:
        return isinstance(candidate(), iface)
