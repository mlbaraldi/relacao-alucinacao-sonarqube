
def histogram(test):
    # Split the string into a list of words
    words = test.split()
    
    # Create an empty dictionary to store the histogram
    histogram_dict = {}
    
    # Iterate over the list of words
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in histogram_dict:
            histogram_dict[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            histogram_dict[word] = 1
    
    # Find the maximum count
    max_count = max(histogram_dict.values())
    
    # Create a new dictionary with words that have the maximum count
    max_count_dict = {word: count for word, count in histogram_dict.items() if count == max_count}
    
    return max_count_dict
