def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    import subprocess
    import sys
    """
    Call the given command(s).
    """
    cmd = commands + args
    if verbose:
        print(f"Running command: {' '.join(cmd)}", file=sys.stderr)
    stderr_param = subprocess.DEVNULL if hide_stderr else None
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        stderr=stderr_param,
    )
    return result.returncode
