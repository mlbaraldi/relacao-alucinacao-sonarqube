
def special_factorial(n):
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * factorial(num - 1)

    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result
