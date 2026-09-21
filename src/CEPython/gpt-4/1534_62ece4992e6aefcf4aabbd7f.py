from urllib.parse import urlparse
from typing import Tuple


def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Parse an image href into composite parts.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
    """
    parsed = urlparse(image_href)

    if not all([parsed.scheme, parsed.netloc, parsed.path]):
        raise ValueError("Invalid image href")

    image_id = parsed.path.rsplit('/', 1)[-1]
    use_ssl = parsed.scheme == 'https'

    return image_id, parsed.netloc, use_ssl
