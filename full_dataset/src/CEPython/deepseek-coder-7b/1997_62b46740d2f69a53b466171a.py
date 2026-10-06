

def pretty(self, indent=0, debug=False):
    """
    Return a pretty formatted representation of self.
    """
    pretty_str = '  ' * indent + f"Name: {self.name}\n"
    pretty_str += '  ' * indent + f"Age: {self.age}\n"
    if debug:
        pretty_str += '  ' * indent + f"Debug info: {self.__dict__}"
    return pretty_str
