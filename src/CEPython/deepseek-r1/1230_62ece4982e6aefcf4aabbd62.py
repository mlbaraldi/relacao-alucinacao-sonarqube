def _replace_url_args(url, url_args):
    import re
    """
    Replace any custom string URL items with values in args
    """
    return re.sub(
        r'\{([^{}]+)\}',
        lambda m: str(url_args.get(m.group(1), m.group(0))),
        url
    )
