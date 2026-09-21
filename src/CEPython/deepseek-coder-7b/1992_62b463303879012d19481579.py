

def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extract the possible values of number and suppl from the contents of issue.
    """
    if isinstance(issue, dict) and 'number' in issue and 'suppl' in issue:
        return issue['number'], issue['suppl']
    else:
        return None, None
