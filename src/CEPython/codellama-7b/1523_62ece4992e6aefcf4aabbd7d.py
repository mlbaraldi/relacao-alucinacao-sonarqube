import subprocess
import os


def subprocess_run_helper(func, *args, timeout, extra_env=None):
    # Create a new environment dictionary with the extra environment variables
    env = os.environ.copy()
    if extra_env is not None:
        env.update(extra_env)

    # Create a new process with the given function and arguments
    process = subprocess.Popen([func.__module__ + '.' + func.__name__] + list(args), env=env)

    # Wait for the process to finish with a timeout
    try:
        process.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        raise TimeoutError('The process timed out after {} seconds'.format(timeout))

    # Check if the process was successful
    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, process.args)

    # Return the output of the process
    return process.stdout.decode('utf-8')
