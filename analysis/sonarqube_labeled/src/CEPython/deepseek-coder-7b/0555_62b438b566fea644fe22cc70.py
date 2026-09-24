import subprocess
import re


def bash_completion():
    """
    Return a bash completion script for the borgmatic command. Produce this by introspecting
    borgmatic's command-line argument parsers.
    """
    # Get the help output from borgmatic
    try:
        help_output = subprocess.check_output(['borgmatic', '--help'], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error getting borgmatic help output: {e.output}")
        return None

    # Extract the subcommands and options from the help output
    subcommands = re.findall(r'  (\w+)', help_output)
    options = re.findall(r'--(\w+)', help_output)

    # Generate the bash completion script
    script = [
        '#!/bin/bash',
        'complete -W "{}" borgmatic'.format(' '.join(subcommands + options))
    ]

    return '\n'.join(script)

# Save the script to a file
