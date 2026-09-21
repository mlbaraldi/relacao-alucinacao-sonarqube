

def next_version(version):
    # Split the version string into its components
    major, minor, patch = version.split('.')

    # Increment the patch version
    patch = int(patch) + 1

    # If the patch version is greater than 9, increment the minor version
    if patch > 9:
        minor = int(minor) + 1
        patch = 0

    # If the minor version is greater than 9, increment the major version
    if minor > 9:
        major = int(major) + 1
        minor = 0

    # Join the components back into a version string
    return f'{major}.{minor}.{patch}'
