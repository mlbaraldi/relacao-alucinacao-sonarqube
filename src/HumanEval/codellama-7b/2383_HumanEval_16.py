

def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    """
    # Convert the string to lowercase to make the comparison case-insensitive
    string = string.lower()

    # Create a set to store the distinct characters
    distinct_chars = set()

    # Iterate over the characters in the string
    for char in string:
        # If the character is not already in the set, add it
        if char not in distinct_chars:
            distinct_chars.add(char)

    # Return the length of the set, which is the number of distinct characters
    return len(distinct_chars)
