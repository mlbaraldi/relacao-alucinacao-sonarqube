def amend_bzparams(self, params, bug_ids):
    """
    Amend the Bugzilla params
    """
    params['id'] = bug_ids
