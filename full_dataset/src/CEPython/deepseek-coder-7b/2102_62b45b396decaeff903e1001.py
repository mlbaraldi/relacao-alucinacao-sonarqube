

def amend_bzparams(self, params, bug_ids):
    """
    Amend the Bugzilla params
    """
    # Check if bug_ids is a list
    if not isinstance(bug_ids, list):
        raise ValueError("bug_ids must be a list")

    # Check if new_params is a dictionary
    if not isinstance(new_params, dict):
        raise ValueError("new_params must be a dictionary")

    # Amend the params
    for bug_id in bug_ids:
        if bug_id in self.params:
            self.params[bug_id].update(new_params)
        else:
            self.params[bug_id] = new_params
