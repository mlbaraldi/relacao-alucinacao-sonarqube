
def odd_count(lst):
    template = "the number of odd elements in the string i of the input."
    result = []
    for s in lst:
        count = sum(1 for c in s if c in {'1', '3', '5', '7', '9'})
        message = template.replace('i', str(count))
        result.append(message)
    return result
