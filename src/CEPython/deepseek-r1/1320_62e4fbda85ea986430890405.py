def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs:
    import os
    import sys
    import subprocess
    from concurrent.futures import ThreadPoolExecutor
    from typing import Sequence
    sum_cmd = sum(len(arg) for arg in cmd)
    len_cmd = len(cmd)
    fixed_value = sum_cmd + (len_cmd - 1)
    remaining_length = _max_length - fixed_value

    if remaining_length < 0:
        raise ValueError(f"Command {cmd} exceeds maximum allowed length {_max_length}")

    chunks = []
    current_chunk = []
    current_total = 0  # Tracks sum(len(arg) + 1 for arg in current_chunk)

    for arg in varargs:
        arg_contribution = len(arg) + 1
        if current_total + arg_contribution <= remaining_length:
            current_chunk.append(arg)
            current_total += arg_contribution
        else:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = []
                current_total = 0
            if arg_contribution > remaining_length:
                raise ValueError(f"Argument {arg} is too long to fit into a command")
            current_chunk.append(arg)
            current_total = arg_contribution
    if current_chunk:
        chunks.append(current_chunk)

    def run_command(command):
        if color and sys.platform != 'win32':
            import pty
            master, slave = pty.openpty()
            try:
                process = subprocess.Popen(
                    command,
                    stdin=slave,
                    stdout=slave,
                    stderr=subprocess.STDOUT,
                    close_fds=True,
                    **kwargs
                )
                os.close(slave)
                while True:
                    try:
                        data = os.read(master, 1024)
                    except OSError:
                        break
                    if not data:
                        break
                    os.write(sys.stdout.fileno(), data)
                process.wait()
                return process.returncode
            finally:
                os.close(master)
        else:
            result = subprocess.run(command, **kwargs)
            return result.returncode

    with ThreadPoolExecutor(max_workers=target_concurrency) as executor:
        futures = []
        for chunk in chunks:
            full_cmd = list(cmd) + chunk
            futures.append(executor.submit(run_command, full_cmd))
        for future in futures:
            future.result()
