
def search(lst):
    # Create a dictionary to store the frequency of each integer
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Iterate over the dictionary in reverse order to find the first integer with frequency greater than or equal to its value
    for num in sorted(freq.keys(), reverse=True):
        if freq[num] >= num:
            return num

    # If no such integer is found, return -1
    return -1
