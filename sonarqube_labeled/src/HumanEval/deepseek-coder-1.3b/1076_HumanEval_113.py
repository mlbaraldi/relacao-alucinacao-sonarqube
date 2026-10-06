
def odd_count(lst):
    result = []
    for i in range(len(lst)):
        count = sum(1 for c in lst[i] if int(c) % 2 != 0)
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(count, i, i, i))
    return result
