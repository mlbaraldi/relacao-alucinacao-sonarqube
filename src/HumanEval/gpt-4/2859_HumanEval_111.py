
def histogram(test):
    # Split the string into a list of letters
    letters = test.split()
    
    # Create a dictionary to store the count of each letter
    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    # Find the maximum count
    max_count = max(letter_counts.values(), default=0)
    
    # Create a new dictionary to store the letters with the maximum count
    max_count_letters = {letter: count for letter, count in letter_counts.items() if count == max_count}
    
    return max_count_letters
