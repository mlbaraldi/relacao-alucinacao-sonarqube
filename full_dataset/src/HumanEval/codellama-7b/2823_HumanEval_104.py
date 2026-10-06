
def unique_digits(x):
    # Initialize an empty list to store the unique digits
    unique_list = []

    # Iterate over the input list
    for num in x:
        # Check if any digit in the current number is even
        for digit in str(num):
            if int(digit) % 2 == 0:
                # If an even digit is found, skip to the next number
                break
        else:
            # If no even digit is found, add the number to the unique list
            unique_list.append(num)

    # Sort the unique list in increasing order
    unique_list.sort()

    return unique_list
