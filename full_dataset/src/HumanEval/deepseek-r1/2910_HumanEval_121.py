
def solution(lst):
    total = 0
    for index, num in enumerate(lst):
        if index % 2 == 0 and num % 2 != 0:
            total += num
    return total
