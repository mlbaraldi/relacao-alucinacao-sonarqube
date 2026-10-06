def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    import subprocess
    """
    Call the given command(s).
    """
    # Convert commands and args to a list of string parts
    cmd = []
    if isinstance(commands, (list, tuple)):
        cmd.extend(str(c) for c in commands)
    else:
        cmd.append(str(commands))
    cmd.extend(str(arg) for arg in args)
    
    # Print the command if verbose is enabled
    if verbose:
        print(f"Running: {' '.join(cmd)}")
    
    # Determine stderr handling
    stderr_param = subprocess.DEVNULL if hide_stderr else None
    
    # Execute the command using subprocess.run
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        stderr=stderr_param,
        stdout=subprocess.PIPE  # Capture stdout to return it
    )
    
    return result
