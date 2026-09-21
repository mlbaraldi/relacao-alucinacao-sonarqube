
def encode(message):
    vowels = 'aeiouAEIOU'
    vowel_shift = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
                   'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_message += vowel_shift[char]
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
    return encoded_message
