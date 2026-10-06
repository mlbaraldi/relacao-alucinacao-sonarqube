
def fruit_distribution(s,n):
    import re
    numbers = re.findall(r'\d+', s)
    apples = int(numbers[0])
    oranges = int(numbers[1])
    return n - apples - oranges
