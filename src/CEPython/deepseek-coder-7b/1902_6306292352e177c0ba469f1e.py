import re


def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    # Regular expression to match URLs
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Find all URLs in the text
    urls = url_pattern.findall(text)

    # Add attributes to URLs
    for url in urls:
        text = text.replace(url, f'<a href="{url}" target="_blank">{url}</a>')

    return text
