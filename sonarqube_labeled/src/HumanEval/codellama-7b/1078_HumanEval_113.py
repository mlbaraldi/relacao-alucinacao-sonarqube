
def odd_count(lst):
    result = []
    for i, s in enumerate(lst):
        count = 0
        for c in s:
            if int(c) % 2 == 1:
                count += 1
        result.append(f"the number of odd elements {count}n the str{i}ng {i} of the {i}nput.")
    return result
