
def encode(message):
    # Swap case of all letters
    message = message.swapcase()

    # Replace vowels with the letter that appears 2 places ahead of that vowel in the English alphabet
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        index = message.find(vowel)
        if index != -1:
            next_letter = message[index + 2]
            message = message.replace(vowel, next_letter)

    return message
