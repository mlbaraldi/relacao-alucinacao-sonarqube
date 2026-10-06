import os


def remove_ending_os_sep(input_list):
    """
    Iterate over a string list and remove trailing os seperator characters.

    Each string is tested if its length is greater than one and if the last
    character is the pathname seperator. If so, the pathname seperator character
    is removed.

    Args:
        input_list: list of strings

    Returns:
        Processed list of strings

    Raises:
        TypeError
    """
    if not isinstance(input_list, list):
        raise TypeError("Input should be a list of strings")

    for i in range(len(input_list)):
        if not isinstance(input_list[i], str):
            raise TypeError("All elements in the list should be strings")

        if len(input_list[i]) > 1 and input_list[i][-1] == os.sep:
            input_list[i] = input_list[i][:-1]

    return input_list
