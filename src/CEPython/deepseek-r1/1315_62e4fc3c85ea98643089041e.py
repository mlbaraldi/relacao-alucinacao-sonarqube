def _inline_r_setup(code: str) -> str:
    """
    Prepends R code to set specific options that cannot be configured via environment variables.
    Sets the width option to a high value to prevent line wrapping in output.
    """
    setup_code = "options(width=10000)\n"
    return setup_code + code
