import subprocess


def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    # Prepare the command
    command = [commands] + args

    # Prepare the subprocess options
    options = {
        'cwd': cwd,
        'env': env,
        'stderr': subprocess.DEVNULL if hide_stderr else None,
        'stdout': subprocess.PIPE,
        'universal_newlines': True,
    }

    # Run the command
    try:
        process = subprocess.run(command, **options)
    except Exception as e:
        print(f"Error running command: {e}")
        return None

    # Print the output if verbose is True
    if verbose:
        print(process.stdout)

    # Return the process
    return process
