

def encode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split the string into groups of three characters each, same as in encode_cyclic
    groups = [s[3 * i : min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    # For each group of three characters, cycle back by moving the last character to the front
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
