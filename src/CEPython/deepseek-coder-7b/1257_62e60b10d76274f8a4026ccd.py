

def data(self, *keys):
    """
    Return the keys and values of this record as a dictionary,
    optionally including only certain values by index or key. Keys
    provided in the items that are not in the record will be
    inserted with a value of :const:`None`; indexes provided
    that are out of bounds will trigger an :exc:`IndexError`.

    :param keys: indexes or keys of the items to include; if none
                  are provided, all values will be included
    :return: dictionary of values, keyed by field name
    :raises: :exc:`IndexError` if an out-of-bounds index is specified
    """
    if not keys:
        return self._data

    result = {}
    for key in keys:
        if isinstance(key, int):
            if key < len(self._data):
                result[list(self._data.keys())[key]] = list(self._data.values())[key]
            else:
                raise IndexError("list index out of range")
        else:
            result[key] = self._data.get(key, None)

    return result
