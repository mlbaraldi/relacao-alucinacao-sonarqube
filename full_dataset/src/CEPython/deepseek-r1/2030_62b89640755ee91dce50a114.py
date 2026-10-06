def tzname_in_python2(namefunc):
    import sys
    if sys.version_info[0] >= 3:
        return namefunc
    else:
        def wrapper(*args, **kwargs):
            result = namefunc(*args, **kwargs)
            if isinstance(result, unicode):
                return result.encode('ascii')
            else:
                return result
        return wrapper
