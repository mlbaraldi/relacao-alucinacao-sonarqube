

def next_version(version):
    # Split the version by the dot
    version_parts = version.split('.')
    
    # Convert each part to an integer
    version_parts = [int(part) for part in version_parts]
    
    # Increment the last part of the version
    version_parts[-1] += 1
    
    # If the last part is now 10, set it to 0 and increment the second to last part
    for i in range(len(version_parts)-1, -1, -1):
        if version_parts[i] == 10:
            version_parts[i] = 0
            if i != 0:
                version_parts[i-1] += 1
            else:
                version_parts.insert(0, 1)
    
    # Convert each part back to a string
    version_parts = [str(part) for part in version_parts]
    
    # Join the parts back together with a dot
    next_version = '.'.join(version_parts)
    
    return next_version
