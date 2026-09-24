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
        'universal_newlines': True,
    }

    # Run the command
    try:
        result = subprocess.run(command, **options)
    except Exception as e:
        if verbose:
            print(f"Command '{commands}' failed with error: {e}")
        return None

    # Print the output if verbose is True
    if verbose:
        print(result.stdout)

    return result
