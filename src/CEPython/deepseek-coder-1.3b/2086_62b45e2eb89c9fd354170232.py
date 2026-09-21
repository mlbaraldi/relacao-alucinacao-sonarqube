

def next_version(version):
    # Split the version string into major, minor, and patch components
    major, minor, patch = map(int, version.split('.'))

    # Increment the patch component by 1
    patch += 1

    # Return the next version string following the existing pattern
    return '.'.join(map(str, [major, minor, patch]))
