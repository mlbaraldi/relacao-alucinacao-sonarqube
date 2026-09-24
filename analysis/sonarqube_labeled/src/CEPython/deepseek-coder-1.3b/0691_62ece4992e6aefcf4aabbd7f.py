from typing import Tuple


def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Parse an image href into composite parts.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
    """

    if not image_href.startswith('http://') and not image_href.startswith('https://'):
        raise ValueError('Invalid image href. It should start with http:// or https://')

    parts = image_href.split('/')

    if len(parts) < 3:
        raise ValueError('Invalid image href. It should contain at least three parts')

    image_id = parts[2]
    netloc = parts[3]

    if ':' in netloc:
        netloc, use_ssl = netloc.split(':')
        use_ssl = use_ssl == 'https'
    else:
        use_ssl = False

    return image_id, netloc, use_ssl
