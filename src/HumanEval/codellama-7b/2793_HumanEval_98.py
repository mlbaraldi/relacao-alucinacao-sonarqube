
def count_upper(s):
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            count += 1
    return count
