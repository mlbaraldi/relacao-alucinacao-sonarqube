import re
from urllib.parse import urlparse, urlunparse


def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    # Regular expression to match URLs
    url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Find all URLs in the text
    urls = re.findall(url_regex, text)

    # Process each URL
    for url in urls:
        # Parse the URL
        parsed_url = urlparse(url)

        # Linkify the URL
        linkified_url = urlunparse(('', '', parsed_url.netloc, parsed_url.path, '', ''))

        # Replace the original URL with the linkified URL
        text = text.replace(url, linkified_url)

    return text
