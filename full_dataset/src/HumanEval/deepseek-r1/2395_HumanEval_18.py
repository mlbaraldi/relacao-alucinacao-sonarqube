

def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    if sub_len == 0:
        return 0
    for i in range(str_len - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count
