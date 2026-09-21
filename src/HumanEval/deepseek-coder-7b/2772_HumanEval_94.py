

def skjkasdkd(lst):
    primes = [x for x in lst if is_prime(x)]
    if not primes:
        return None
    largest_prime = max(primes)
    return sum(int(digit) for digit in str(largest_prime))

# Test cases
