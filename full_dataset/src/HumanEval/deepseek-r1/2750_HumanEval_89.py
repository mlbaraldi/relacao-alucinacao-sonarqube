
def encrypt(s):
    encrypted = []
    for c in s:
        if 'a' <= c <= 'z':
            shifted = (ord(c) - ord('a') + 4) % 26
            encrypted_char = chr(shifted + ord('a'))
            encrypted.append(encrypted_char)
        else:
            encrypted.append(c)
    return ''.join(encrypted)
