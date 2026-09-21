

def sort_third(l: list):
    # Extract the elements at indices divisible by 3
    third_elements = [l[i] for i in range(0, len(l), 3)]
    # Sort the extracted elements
    third_elements.sort()
    
    # Replace the elements at indices divisible by 3 with the sorted elements
    for i, val in enumerate(third_elements):
        l[i*3] = val
    
    return l
