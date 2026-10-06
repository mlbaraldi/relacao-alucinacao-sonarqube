

def remove_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_text = ''
    for char in text:
        if char not in vowels:
            new_text += char
    return new_text
