def validate_requires_args(self, args):
    """
    Check if all the required arguments have been provided.
    """
    missing = []
    for arg in self.required_args:
        if isinstance(args, dict):
            present = arg in args
        else:
            present = hasattr(args, arg)
        if not present:
            missing.append(arg)
    if missing:
        raise ValueError(f"Missing required arguments: {', '.join(missing)}")
