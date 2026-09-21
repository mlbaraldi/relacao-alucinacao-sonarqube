def addignored(ignored):
    import subprocess
    """
    Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
    """
    # Execute the git command to get ignored files
    output = subprocess.check_output(
        ['git', 'ls-files', '--others', '--ignored', '--exclude-standard']
    )
    # Decode the output from bytes to string and split into lines
    files = output.decode('utf-8').strip().split('\n')
    # Sort the list of filenames
    files.sort()
    # Join the sorted filenames with commas and return
    return ','.join(files)
