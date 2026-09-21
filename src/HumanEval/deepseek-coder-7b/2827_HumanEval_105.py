
def by_length(arr):
    # Filter the array to only include numbers between 1 and 9
    arr = [i for i in arr if 0 < i < 10]
    
    # Sort the array in ascending order
    arr.sort()
    
    # Reverse the array
    arr.reverse()
    
    # Map each number to its corresponding name
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    arr = [names[i-1] for i in arr]
    
    return arr
