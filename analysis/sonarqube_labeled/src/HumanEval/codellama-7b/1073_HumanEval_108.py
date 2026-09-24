
def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            count += 1
        else:
            count += sum(map(abs, str(num))) > 0
    return count
