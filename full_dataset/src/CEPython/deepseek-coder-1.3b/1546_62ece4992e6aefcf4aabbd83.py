import subprocess


def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    cmd = ' '.join(commands)
    cmd_args = args.split()

    process = subprocess.Popen(
        cmd,
        cmd_args,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        env=env
    )

    stdout, stderr = process.communicate()

    if verbose:
        print(f'Command: {cmd} {" ".join(cmd_args)}')
        print(f'Output: {stdout}')
        if stderr:
            print(f'Error: {stderr}')

    return stdout, stderr
