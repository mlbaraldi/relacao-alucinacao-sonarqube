from bs4 import BeautifulSoup
import re


def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    # Find all URLs in the text
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(text, 'html.parser')
    
    # For each URL, create a new link tag with the URL as the href attribute
    for url in urls:
        link = soup.new_tag('a', href=url, target='_blank')
        link.string = url
        text = text.replace(url, str(link))
    
    return text
