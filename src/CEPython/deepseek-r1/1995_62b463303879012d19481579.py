def _extract_number_and_supplment_from_issue_element(issue):
    import re
    """
    Extract the possible values of number and suppl from the contents of issue.
    """
    number = None
    suppl = None

    # Split the issue into parts before and after 'Suppl' (case-insensitive)
    match = re.search(r'^(.*?)Suppl(.*)$', issue, re.IGNORECASE)
    if match:
        before = match.group(1).strip()
        after = match.group(2).strip()
    else:
        before = issue.strip()
        after = ''

    # Extract number from the before part
    if before:
        num_match = re.search(r'\d+', before)
        if num_match:
            number = int(num_match.group())

    # Extract suppl from the after part
    if after:
        suppl_match = re.search(r'\d+', after)
        if suppl_match:
            suppl = int(suppl_match.group())

    return number, suppl
