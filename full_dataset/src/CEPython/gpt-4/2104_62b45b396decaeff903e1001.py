

def amend_bzparams(self, params, bug_ids):
    """
    Amend the Bugzilla params
    """
    if not isinstance(params, dict):
        raise ValueError("params should be a dictionary")

    if not isinstance(bug_ids, list):
        raise ValueError("bug_ids should be a list")

    # Assuming params is a dictionary and bug_ids is a list of bug ids
    params['bug_id'] = bug_ids

    return params
