
def find_max(words):
    # Initialize max_unique_chars to 0 and max_word to empty string
    max_unique_chars = 0
    max_word = ''

    # Sort the words in lexicographical order
    words.sort()

    # Iterate over each word in the list
    for word in words:
        # Count the number of unique characters in the word
        unique_chars = len(set(word))

        # If the number of unique characters is greater than max_unique_chars
        if unique_chars > max_unique_chars:
            # Update max_unique_chars and max_word
            max_unique_chars = unique_chars
            max_word = word

    # Return the word with maximum number of unique characters
    return max_word
