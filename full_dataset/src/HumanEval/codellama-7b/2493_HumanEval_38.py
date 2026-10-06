

def encode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split the input string into groups of three characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Decode the cycled groups by reversing the cycling operation.
    groups = [(group[0] + group[1:]) if len(group) == 3 else group for group in groups]
    
    # Join the decoded groups back into a single string.
    return "".join(groups)
