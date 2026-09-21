
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    """
    # Split the input string into a list of individual letters
    letters = test.split()

    # Create an empty dictionary to store the letter counts
    letter_counts = {}

    # Iterate over the list of letters and increment the count for each letter
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # Sort the dictionary by value (count) in descending order
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    # If there are multiple letters with the same count, return all of them
    if len(sorted_letter_counts) > 1 and sorted_letter_counts[0][1] == sorted_letter_counts[1][1]:
        return {letter: count for letter, count in sorted_letter_counts}

    # Otherwise, return the letter with the highest count
    return {sorted_letter_counts[0][0]: sorted_letter_counts[0][1]}
