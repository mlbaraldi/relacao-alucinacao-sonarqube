
def encode(message):
    """
    Encodes the message by swapping the case of all letters and replacing vowels with the next two letters in the alphabet.
    """
    swapped = message.swapcase()
    result = []
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    for char in swapped:
        if char in vowels:
            shifted_char = chr(ord(char) + 2)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)
