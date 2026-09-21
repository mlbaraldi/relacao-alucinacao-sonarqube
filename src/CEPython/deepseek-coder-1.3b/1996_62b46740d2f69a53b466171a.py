

def pretty(self, indent=0, debug=False):
    """
    Return a pretty formatted representation of self.
    """
    class_name = self.__class__.__name__
    indentation = " " * indent
    result = f"{indentation}<{class_name} object>\n"

    for key, value in self.__dict__.items():
        if isinstance(value, object):
            if debug:
                result += f"{indentation}  {key}: <{value.__class__.__name__} object>\n"
            else:
                result += f"{indentation}  {key}: <{value.__class__.__name__}>\n"
        else:
            if debug:
                result += f"{indentation}  {key}: {value}\n"
            else:
                result += f"{indentation}  {key}: {value.__repr__()}\n"

    for key, value in self.__dict__.items():
        if isinstance(value, object):
            result += f"{pretty(value, indent+4, debug).rstrip()}\n"

    return result.rstrip()
