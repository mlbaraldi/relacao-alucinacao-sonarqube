import sys


def tzname_in_python2(namefunc):
    """
    Change unicode output into bytestrings in Python 2

    tzname() API changed in Python 3. It used to return bytes, but was changed
    to unicode strings
    """
    if sys.version_info[0] == 2:
        return namefunc().encode('utf-8')
    else:
        return namefunc()
