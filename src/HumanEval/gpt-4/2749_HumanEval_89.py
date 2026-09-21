
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shift = 2 * 2
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result
