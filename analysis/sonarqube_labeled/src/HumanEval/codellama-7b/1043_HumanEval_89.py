
def encrypt(s):
    # Rotate the alphabet by 2 places
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotated_alphabet = alphabet[2:] + alphabet[:2]

    # Replace each letter in the input string with the corresponding letter in the rotated alphabet
    encrypted_string = ""
    for letter in s:
        if letter in alphabet:
            encrypted_string += rotated_alphabet[alphabet.index(letter)]
        else:
            encrypted_string += letter

    return encrypted_string
