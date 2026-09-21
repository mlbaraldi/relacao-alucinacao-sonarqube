def process_text_links(text):
    import re
    from bs4 import BeautifulSoup
    """
    Process links in text, adding target="_blank" and rel="noopener noreferrer" to existing links,
    and convert textual URLs into clickable links with the same attributes.
    """
    soup = BeautifulSoup(text, 'html.parser')
    
    # Add attributes to existing <a> tags
    for a_tag in soup.find_all('a'):
        a_tag['target'] = '_blank'
        a_tag['rel'] = 'noopener noreferrer'
    
    # Regular expression to find URLs starting with http:// or https://
    url_regex = re.compile(r'https?://\S+')
    
    # Process each text node to replace URLs with <a> tags
    for text_node in soup.find_all(text=True):
        if text_node.parent.name == 'a':
            continue  # Skip text inside existing <a> tags
        
        parent = text_node.parent
        if not parent:
            continue
        
        content = str(text_node)
        parts = []
        last_pos = 0
        
        for match in url_regex.finditer(content):
            start = match.start()
            end = match.end()
            url = match.group()
            
            # Add text before the URL
            if start > last_pos:
                parts.append(content[last_pos:start])
            
            # Create new <a> tag for the URL
            new_a_tag = soup.new_tag('a', href=url)
            new_a_tag['target'] = '_blank'
            new_a_tag['rel'] = 'noopener noreferrer'
            new_a_tag.string = url
            parts.append(new_a_tag)
            
            last_pos = end
        
        # Add remaining text after the last URL
        if last_pos < len(content):
            parts.append(content[last_pos:])
        
        # Replace the original text node with the new elements
        text_node.replace_with(*parts)
    
    return str(soup)
