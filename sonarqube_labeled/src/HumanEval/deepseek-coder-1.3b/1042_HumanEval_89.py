
def encrypt(s):
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            shift = 2
            if char.isupper():
                shift = ord(char) - ord('A') + shift
                shift %= 26
                encrypted_string += chr(ord('A') + shift)
            else:
                shift = ord(char) - ord('a') + shift
                shift %= 26
                encrypted_string += chr(ord('a') + shift)
        else:
            encrypted_string += char
    return encrypted_string
