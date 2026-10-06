import subprocess


def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if not isinstance(commands, list):
        commands = [commands]

    if not isinstance(args, list):
        args = [args]

    if cwd is not None and not isinstance(cwd, str):
        raise ValueError("cwd must be a string")

    if verbose and hide_stderr:
        raise ValueError("verbose and hide_stderr cannot both be True")

    if env is not None and not isinstance(env, dict):
        raise ValueError("env must be a dictionary")

    for command in commands:
        if not isinstance(command, str):
            raise ValueError("commands must be a list of strings")

    for arg in args:
        if not isinstance(arg, str):
            raise ValueError("args must be a list of strings")

    if verbose:
        print("Running command:", " ".join(commands))

    if hide_stderr:
        stderr = subprocess.DEVNULL
    else:
        stderr = subprocess.PIPE

    if env is not None:
        env = {**os.environ, **env}

    process = subprocess.Popen(commands, args, cwd=cwd, stderr=stderr, env=env)
    output, error = process.communicate()

    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, commands)

    if verbose:
        print("Command output:", output)

    return output
