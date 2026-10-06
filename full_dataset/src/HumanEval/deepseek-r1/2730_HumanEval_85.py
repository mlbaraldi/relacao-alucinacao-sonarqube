
def add(lst):
    total = 0
    for index in range(len(lst)):
        if index % 2 == 1:
            if lst[index] % 2 == 0:
                total += lst[index]
    return total
