

def _inline_r_setup(code: str) -> str:
    """
    Some behaviour of R cannot be configured via env variables, but can
    only be configured via R options once R has started. These are set here.
    """
    # Define the R options you want to set up
    r_options = """
    options(scipen=999)
    options(stringsAsFactors=FALSE)
    """

    # Combine the R options with the provided code
    r_code = r_options + "\n" + code

    return r_code
