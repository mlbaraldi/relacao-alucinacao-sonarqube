

def _replace_url_args(url, url_args):
    """
    Replace any custom string URL items with values in args
    """
    for arg, value in url_args.items():
        url = url.replace('{' + arg + '}', value)
    return url
