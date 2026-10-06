
def by_length(arr):
    # Step 1: Filter the array to include only numbers between 1 and 9 inclusive
    filtered = [x for x in arr if 1 <= x <= 9]
    
    # Step 2: Sort the filtered list in ascending order
    sorted_list = sorted(filtered)
    
    # Step 3: Reverse the sorted list to get descending order
    reversed_list = sorted_list[::-1]
    
    # Step 4: Map each number to its corresponding name
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = [names[num - 1] for num in reversed_list]
    
    return result
