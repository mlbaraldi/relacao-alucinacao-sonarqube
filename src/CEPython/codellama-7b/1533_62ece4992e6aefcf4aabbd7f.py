

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Parse an image href into composite parts.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
    """
    try:
        image_id, netloc, use_ssl = image_href.split('/')
        return image_id, netloc, use_ssl
    except ValueError:
        raise ValueError("Invalid image href: {}".format(image_href))
