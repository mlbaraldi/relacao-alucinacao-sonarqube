
def odd_count(lst):
    result = []
    for i, s in enumerate(lst):
        count = sum(int(c) % 2 for c in s)
        result.append(f"the number of odd elements {count}n the str{i}ng {i} of the {count}nput.")
    return result
