import subprocess


def addignored(ignored):
    # Use git command to get the list of ignored files
    result = subprocess.run(['git', 'ls-files', '--others', '--ignored', '--exclude-standard'], stdout=subprocess.PIPE)
    
    # Decode the output from bytes to string and split it into a list
    files = result.stdout.decode('utf-8').split('\n')
    
    # Filter the list for only ignored files
    ignored_files = [file for file in files if file in ignored]
    
    # Sort the list
    ignored_files.sort()
    
    # Join the list into a single string with each filename separated by a comma
    ignored_files_str = ', '.join(ignored_files)
    
    return ignored_files_str
