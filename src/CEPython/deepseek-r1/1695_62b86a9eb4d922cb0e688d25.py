def _get_resource_name_regex():
    import re
    """
    Build or return the regular expressions that are used to validate
    the name of the Krake resources.

    Returns:
        re.Pattern: the compiled regular expressions, to validate
        the resource name.
    """
    pattern = r"""
        ^                  # Start of the string
        (?=.{1,253}$)      # Ensure the entire string is 1-253 characters long
        [a-z0-9]           # First character must be lowercase alphanumeric
        (?:                # Non-capturing group for the remaining characters
            [a-z0-9.-]*    # Allow lowercase alphanumeric, hyphens, and dots
            [a-z0-9]       # Last character must be lowercase alphanumeric
        )?                 # The remaining part is optional (for single char names)
        $                  # End of the string
    """
    return re.compile(pattern, re.VERBOSE)
