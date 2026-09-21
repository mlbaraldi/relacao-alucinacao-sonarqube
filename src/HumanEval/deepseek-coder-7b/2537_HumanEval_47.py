

def median(l: list):
    sorted_list = sorted(l)
    list_length = len(sorted_list)
    if list_length % 2 == 0:
        return (sorted_list[list_length // 2 - 1] + sorted_list[list_length // 2]) / 2
    else:
        return sorted_list[list_length // 2]

# Test cases
