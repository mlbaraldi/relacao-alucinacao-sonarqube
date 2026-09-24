import subprocess


def addignored(ignored):
Sure, I can help you with that. However, please note that the function `addignored` is not defined in the provided context. I'll assume that you're asking for a function that uses the `git` command to obtain the file names, turns it into a list, sorts the list for only ignored files, and returns those files as a single string with each filename separated by a comma.

Here is a Python function that does that:

```python
import subprocess

def add_ignored(ignored):
    """
    Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
    """
    # Use the git command to obtain the file names
    result = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], stdout=subprocess.PIPE, text=True)
    files = result.stdout.split('\n')

    # Filter out the ignored files
    ignored_files = [file for file in files if file in ignored]

    # Sort the list for only ignored files
    ignored_files.sort()

    # Return those files as a single string with each filename separated by a comma
    return ', '.join(ignored_files)
