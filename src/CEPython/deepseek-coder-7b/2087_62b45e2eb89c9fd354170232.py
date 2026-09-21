

def next_version(version):
    # Split the version into parts
    parts = version.split('.')

    # Increment the last part
    parts[-1] = str(int(parts[-1]) + 1)

    # If the last part is now '10' or more, reset it to '0' and increment the second-to-last part
    if int(parts[-1]) >= 10:
        parts[-1] = '0'
        parts[-2] = str(int(parts[-2]) + 1)

        # If the second-to-last part is now '10' or more, reset it to '0' and increment the third-to-last part
        if int(parts[-2]) >= 10:
            parts[-2] = '0'
            parts[-3] = str(int(parts[-3]) + 1)

    # Join the parts back together
    return '.'.join(parts)
