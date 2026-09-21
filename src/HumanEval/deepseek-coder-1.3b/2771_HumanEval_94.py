

def skjkasdkd(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    largest_prime = max(filter(is_prime, lst))
    return sum_of_digits(largest_prime)
