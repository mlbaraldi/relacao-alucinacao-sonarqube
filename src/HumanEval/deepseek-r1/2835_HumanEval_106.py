
def f(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            # Compute factorial of i
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            result.append(factorial)
        else:
            # Compute sum from 1 to i
            sum_i = i * (i + 1) // 2
            result.append(sum_i)
    return result
