
def search(lst):
    from collections import Counter
    count = Counter(lst)
    max_val = -1
    for num, freq in count.items():
        if num <= freq and num > max_val:
            max_val = num
    return max_val
