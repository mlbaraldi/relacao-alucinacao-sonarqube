

def index(self, key):
    """
    Return the index of the given item.

    :param key: a key
    :return: index
    :rtype: int
    """
    try:
        return self.data.index(key)
    except ValueError:
        return -1  # or raise an exception, or return None, depending on your needs
