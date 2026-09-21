import os


def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Fixes for the following issues on windows
    - https://bugs.python.org/issue8557
    - windows does not parse shebangs

    This function also makes deep-path shebangs work just fine
    """
    # Convert the command tuple to a list for easier manipulation
    cmd_list = list(cmd)
    
    # Normalize the command by ensuring it's a full path and is quoted if necessary
    for i, arg in enumerate(cmd_list):
        # Check if the argument is a shebang and needs to be normalized
        if arg.startswith('#!'):
            # Normalize the shebang by ensuring it's a full path
            shebang = arg.split(' ', 1)[0]
            shebang_path = os.path.normpath(shebang[2:])
            cmd_list[i] = f'{shebang_path} {arg[len(shebang):]}'
        else:
            # Quote the argument if it contains spaces
            if ' ' in arg:
                cmd_list[i] = f'"{arg}"'
    
    # Convert the list back to a tuple and return
    return tuple(cmd_list)

# Example usage:
