def oneline(script, seperator=" && "):
    commands = []
    current_command = []
    for line in script.splitlines():
        stripped = line.rstrip()
        if stripped.endswith('\\'):
            part = stripped[:-1].rstrip()
            current_command.append(part)
        else:
            current_command.append(stripped)
            full_cmd = ' '.join(current_command).strip()
            if full_cmd:
                commands.append(full_cmd)
            current_command = []
    if current_command:
        full_cmd = ' '.join(current_command).strip()
        if full_cmd:
            commands.append(full_cmd)
    return separator.join(commands)
