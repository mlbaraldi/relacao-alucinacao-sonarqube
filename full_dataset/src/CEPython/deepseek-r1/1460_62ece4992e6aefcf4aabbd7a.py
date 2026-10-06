def is_gitbash():
    import os
    import platform
    """Returns True if running in a Windows Git Bash environment."""
    if platform.system() != 'Windows':
        return False
    env = os.environ
    return ('MSYSTEM' in env or
            env.get('TERM_PROGRAM') == 'mintty' or
            env.get('OSTYPE') == 'msys')
