import concurrent.futures
import os
import pty
import subprocess
import sys
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
