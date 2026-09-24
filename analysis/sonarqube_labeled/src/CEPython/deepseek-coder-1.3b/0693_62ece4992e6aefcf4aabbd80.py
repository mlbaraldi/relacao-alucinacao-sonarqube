

def remove_ending_os_sep(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input should be a list")
    for i in range(len(input_list)):
        if isinstance(input_list[i], str) and len(input_list[i]) > 1 and input_list[i][-1] == "\\":
            input_list[i] = input_list[i][:-1]
    return input_list
