import urllib.parse


def _replace_url_args(url, url_args):
    """
    Replace any custom string URL items with values in args
    """
    parsed_url = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed_url.query)

    for key, value in url_args.items():
        if key in query:
            query[key] = [value]
        else:
            query[key] = value

    replaced_url = parsed_url._replace(query=urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, urllib.parse.urlencode(query, doseq=True), parsed_url.fragment)))

    return replaced_url
