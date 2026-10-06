

def _inline_r_setup(code: str) -> str:
    """
    Some behaviour of R cannot be configured via env variables, but can
    only be configured via R options once R has started. These are set here.
    """
    # Assuming we want to set an option "max.print" to 100
    option_code = "options(max.print=100)\n"
    return option_code + code
