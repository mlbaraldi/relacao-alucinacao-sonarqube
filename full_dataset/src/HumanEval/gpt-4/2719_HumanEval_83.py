
def starts_one_ends(n):
    if n == 1:
        return 1
    else:
        # There are 10^(n-1) numbers of n digits. 
        # Among them, 2*9^(n-1) numbers start or end with 1.
        # So, we subtract the numbers that start and end with 1, which is 2*8^(n-2)
        return 2 * (10**(n-1) - 9**(n-1)) + 2 * 8**(n-2)
