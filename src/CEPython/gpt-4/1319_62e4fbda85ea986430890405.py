import subprocess
from multiprocessing import Pool
from typing import Sequence


def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs:
    """
    A simplified implementation of xargs.

    color: Make a pty if on a platform that supports it
    target_concurrency: Target number of partitions to run concurrently
    """

    def run_cmd(args):
        full_cmd = list(cmd) + [args]
        return subprocess.run(full_cmd, **kwargs)

    with Pool(target_concurrency) as p:
        p.map(run_cmd, varargs)
