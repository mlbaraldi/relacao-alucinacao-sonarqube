
def by_length(arr):
    # Define the mapping from integer to its corresponding name
    num_to_name = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

    # Filter the array to only include integers between 1 and 9 inclusive
    arr = [i for i in arr if 1 <= i <= 9]

    # Sort the array in reverse order
    arr.sort(reverse=True)

    # Replace each integer by its corresponding name
    arr = [num_to_name[i] for i in arr]

    return arr
