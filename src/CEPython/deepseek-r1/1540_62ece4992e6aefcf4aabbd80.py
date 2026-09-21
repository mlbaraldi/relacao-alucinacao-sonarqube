def remove_ending_os_sep(input_list):
    import os
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
        raise TypeError("input_list must be a list")
    processed = []
    for s in input_list:
        if not isinstance(s, str):
            raise TypeError("All elements must be strings")
        if len(s) > 1 and s.endswith(os.sep):
            processed.append(s[:-1])
        else:
            processed.append(s)
    return processed
