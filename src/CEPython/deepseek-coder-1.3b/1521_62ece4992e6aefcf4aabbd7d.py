import subprocess


def subprocess_run_helper(func, *args, timeout, extra_env=None):
    """
    Run a function in a sub-process.

    Parameters
    ----------
    func : function
        The function to be run.  It must be in a module that is importable.
    *args : str
        Any additional command line arguments to be passed in
        the first argument to ``subprocess.run``.
    extra_env : dict[str, str]
        Any additional environment variables to be set for the subprocess.
    """

    # Create a new process
    process = subprocess.run(
        [func.__module__ + "." + func.__name__] + list(args),
        env=extra_env,
        timeout=timeout
    )

    # Check if the process was successful
    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, process.args)

    # Return the output
    return process.stdout.decode('utf-8')
