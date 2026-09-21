
def special_factorial(n):
    product = 1
    current_fact = 1
    for i in range(1, n + 1):
        current_fact *= i
        product *= current_fact
    return product
