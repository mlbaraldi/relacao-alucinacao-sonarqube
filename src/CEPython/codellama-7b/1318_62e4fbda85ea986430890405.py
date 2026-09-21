import os
import subprocess
import threading


def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs:
    # Create a pty if on a platform that supports it and color is True
    if color and os.name == 'posix':
        master, slave = os.openpty()
        os.close(master)
        os.close(slave)
        cmd = (cmd[0], *cmd[1:], '--color', 'always')

    # Split the varargs into chunks based on the target concurrency
    chunks = [varargs[i:i+target_concurrency] for i in range(0, len(varargs), target_concurrency)]

    # Create a thread pool to run the commands concurrently
    pool = threading.ThreadPool(target_concurrency)

    # Submit the commands to the thread pool
    for chunk in chunks:
        pool.submit(subprocess.run, cmd, chunk, **kwargs)

    # Wait for all the commands to finish
    pool.join()
