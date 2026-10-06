def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    from urllib.parse import urlparse
    from typing import Tuple
    """
    Parse an image href into composite parts.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError: if the image ID cannot be determined from the href
    """
    parsed = urlparse(image_href)
    path = parsed.path
    parts = [part for part in path.split('/') if part]
    
    if not parts:
        raise ValueError("Image ID not found in href")
    
    image_id = parts[-1]
    netloc = parsed.netloc
    use_ssl = (parsed.scheme == 'https')
    
    return (image_id, netloc, use_ssl)
