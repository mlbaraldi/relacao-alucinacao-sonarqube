import re


def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extract the possible values of number and suppl from the contents of issue.
    """
    # Split the issue into parts
    parts = issue.split()

    # Initialize number and suppl to None
    number = None
    suppl = None

    # If there are parts, the first part should be the number
    if len(parts) > 0:
        number = parts[0]

    # If there are more than one parts, the second part should be the suppl
    if len(parts) > 1:
        suppl = parts[1]

    # Return the number and suppl
    return number, suppl
