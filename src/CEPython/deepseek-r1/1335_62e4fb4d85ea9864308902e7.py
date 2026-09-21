def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    import os
    import shlex
    if not cmd:
        return cmd
    script = cmd[0]
    if not os.path.isfile(script):
        return cmd
    try:
        with open(script, 'rb') as f:
            first_line = f.readline().decode('utf-8', errors='ignore').strip()
    except OSError:
        return cmd
    if not first_line.startswith('#!'):
        return cmd
    shebang_line = first_line[2:].strip()
    if not shebang_line:
        return cmd
    try:
        parts = shlex.split(shebang_line)
    except ValueError:
        return cmd
    if not parts:
        return cmd
    interpreter = parts[0]
    args = parts[1:]
    return tuple([interpreter] + args + [script] + list(cmd[1:]))
