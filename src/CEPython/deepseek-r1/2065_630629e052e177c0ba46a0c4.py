def parse_diaspora_webfinger(document: str) -> Dict:
    import json
    import xml.etree.ElementTree as ET
    from typing import Dict
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).
    Returns a dictionary with 'seed_url' and 'guid' keys.
    """
    result = {'seed_url': None, 'guid': None}
    
    # Attempt to parse as JSON first
    try:
        data = json.loads(document)
        links = data.get('links', [])
        for link in links:
            rel = link.get('rel')
            href = link.get('href')
            if rel == 'http://joindiaspora.com/seed_location':
                result['seed_url'] = href
            elif rel == 'http://joindiaspora.com/guid':
                result['guid'] = href
        return result
    except json.JSONDecodeError:
        pass  # Not JSON, proceed to parse as XML
    
    # Attempt to parse as XML/XRD
    try:
        root = ET.fromstring(document)
        for link in root.findall('Link'):
            rel = link.attrib.get('rel')
            href = link.attrib.get('href')
            if rel == 'http://joindiaspora.com/seed_location':
                result['seed_url'] = href
            elif rel == 'http://joindiaspora.com/guid':
                result['guid'] = href
        return result
    except ET.ParseError:
        pass  # Invalid XML
    
    return result
