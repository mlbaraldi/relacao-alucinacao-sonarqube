def subprocess_run_helper(func, *args, timeout, extra_env=None):
    import sys
    import subprocess
    import os
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
    # Extract module and qualified name from the function
    module_name = func.__module__
    qualname = func.__qualname__
    parts = qualname.split('.')
    
    # Generate the code to execute in the subprocess
    code_lines = [
        "import sys, importlib",
        f"module = importlib.import_module({repr(module_name)})",
        "obj = module",
        f"for part in {repr(parts)}:",
        "    obj = getattr(obj, part)",
        "args = sys.argv[1:]",
        "result = obj(*args)",
        "sys.exit(result)"
    ]
    code_str = '\n'.join(code_lines)
    
    # Build the command line
    cmd = [sys.executable, '-c', code_str]
    cmd.extend(args)
    
    # Prepare the environment variables
    env = os.environ.copy()
    if extra_env is not None:
        env.update(extra_env)
    
    # Run the subprocess
    return subprocess.run(cmd, timeout=timeout, env=env)
