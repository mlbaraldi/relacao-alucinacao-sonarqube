import os


def remove_ending_os_sep(input_list):
    if not isinstance(input_list, list):
        raise TypeError("input_list must be a list")

    output_list = []
    for item in input_list:
        if len(item) > 1 and item[-1] == os.sep:
            output_list.append(item[:-1])
        else:
            output_list.append(item)

    return output_list
