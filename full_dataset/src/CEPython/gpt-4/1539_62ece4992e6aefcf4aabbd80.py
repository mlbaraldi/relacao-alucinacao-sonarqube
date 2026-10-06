import os


def remove_ending_os_sep(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input should be a list of strings")

    for i in range(len(input_list)):
        if isinstance(input_list[i], str) and len(input_list[i]) > 1 and input_list[i][-1] == os.sep:
            input_list[i] = input_list[i][:-1]
        elif not isinstance(input_list[i], str):
            raise TypeError("All elements in the list should be strings")

    return input_list
