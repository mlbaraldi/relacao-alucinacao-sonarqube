import subprocess
import os


def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]

    for command in commands:
        if verbose:
            print(f'Running command: {command}')

        if env:
            env = {**os.environ, **env}

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=(subprocess.PIPE if not hide_stderr else None),
            cwd=cwd,
            env=env,
            shell=True
        )

        output, errors = process.communicate()

        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, command, output, errors)

        if verbose:
            print(f'Command output: {output}')

        if args:
            return output
