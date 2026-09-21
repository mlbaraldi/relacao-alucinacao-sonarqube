
def is_sorted(lst):
    # Check if the list is sorted in ascending order
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    
    # Check for elements appearing more than twice
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
            if freq[num] > 2:
                return False
        else:
            freq[num] = 1
    
    return True
