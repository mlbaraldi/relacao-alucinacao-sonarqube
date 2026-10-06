import subprocess


def addignored(ignored):
    """
    Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
    """
    # Execute the 'git ls-files' command to get the list of files
    # Then filter out the ignored files based on the provided list
    # Finally, join the filenames into a single string separated by commas
    try:
        # Execute the git command
        result = subprocess.run(['git', 'ls-files', '--ignored', '--exclude-standard'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Split the output into a list of filenames
            filenames = result.stdout.splitlines()

            # Filter the filenames based on the provided list of ignored files
            ignored_files = [filename for filename in filenames if filename in ignored]

            # Sort the list of ignored files
            ignored_files.sort()

            # Join the filenames into a single string separated by commas
            return ', '.join(ignored_files)
        else:
            # If the command was not successful, print the error message
            print(f"Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
