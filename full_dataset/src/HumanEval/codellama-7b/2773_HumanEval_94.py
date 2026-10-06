

def skjkasdkd(lst):
    # Find the largest prime value in the list
    largest_prime = None
    for i in range(len(lst)):
        if is_prime(lst[i]):
            largest_prime = lst[i]
            break

    # Return the sum of the digits of the largest prime value
    if largest_prime is not None:
        return sum(map(int, str(largest_prime)))
    else:
        return 0

