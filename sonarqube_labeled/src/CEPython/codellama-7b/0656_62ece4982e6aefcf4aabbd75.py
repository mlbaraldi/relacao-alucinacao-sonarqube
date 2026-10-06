import subprocess


def addignored(ignored):
    # Use the git command to obtain the file names
    file_names = subprocess.check_output(['git', 'ls-files', '--ignored']).decode().splitlines()

    # Turn the file names into a list
    file_names_list = [file_name.strip() for file_name in file_names]

    # Sort the list of file names
    file_names_list.sort()

    # Return the list of file names as a single string with each filename separated by a comma
    return ', '.join(file_names_list)
