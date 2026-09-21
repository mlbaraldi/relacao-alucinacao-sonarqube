
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char in vowels:
            if char.isupper():
                encoded_message += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
            else:
                encoded_message += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            if char.isupper():
                encoded_message += char.lower()
            else:
                encoded_message += char.upper()
    return encoded_message
