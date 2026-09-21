
def get_odd_collatz(n):
    # Initialize the list with the input number
    collatz_sequence = [n]
    
    # Generate the Collatz sequence
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_sequence.append(n)
    
    # Filter the odd numbers and sort them
    odd_collatz = sorted([num for num in collatz_sequence if num % 2 != 0])
    
    return odd_collatz
