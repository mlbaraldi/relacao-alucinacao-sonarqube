

def tzname_in_python2(namefunc):
    if namefunc is None:
        return None
    else:
        return namefunc().encode('utf-8')
