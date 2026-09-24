
def encode(message):
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            index = vowels.index(char.lower())
            if char.isupper():
                encoded_message += chr(ord('A') + (index + 2) % 26)
            else:
                encoded_message += chr(ord('a') + (index + 2) % 26)
        else:
            encoded_message += char
    return encoded_message
