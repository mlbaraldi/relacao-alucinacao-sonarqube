
def count_upper(s):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    count = 0
    for idx, char in enumerate(s):
        if idx % 2 == 0 and char in vowels:
            count += 1
    return count
