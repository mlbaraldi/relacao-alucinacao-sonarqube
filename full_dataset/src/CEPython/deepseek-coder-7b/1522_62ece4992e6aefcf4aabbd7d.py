import subprocess
import sys


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
    timeout : int, optional
        The maximum number of seconds to wait for the subprocess.
    extra_env : dict[str, str], optional
        Any additional environment variables to be set for the subprocess.
    """
    # Prepare the command to be run in the subprocess
    command = [sys.executable, '-c', func.__module__ + '.' + func.__name__] + list(args)
    
    # Prepare the environment variables
    env = dict(os.environ)
    if extra_env:
        env.update(extra_env)
    
    # Run the subprocess
    try:
        result = subprocess.run(command, env=env, timeout=timeout, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.TimeoutExpired:
        print("The subprocess timed out.")
        return None
    except subprocess.CalledProcessError as e:
        print(f"The subprocess failed with return code {e.returncode}.")
        return None
