def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None,
                     extra_vars=None, ansible_args=None):
    import subprocess
    import json
    import sys
    """
    Wraps the 'ansible-playbook' CLI.

    :param ir_workspace: An Infrared Workspace object represents the active workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :param playbook_path: the playbook to invoke
    :param verbose: Ansible verbosity level
    :param extra_vars: dict. Passed to Ansible as extra-vars
    :param ansible_args: dict of ansible-playbook arguments to plumb down directly to Ansible.
    """
    cmd = ['ansible-playbook']

    # Handle verbosity
    if verbose is not None and verbose > 0:
        cmd.append('-' + 'v' * verbose)

    # Handle extra_vars
    if extra_vars is not None:
        cmd.extend(['--extra-vars', json.dumps(extra_vars)])

    # Handle ansible_args
    if ansible_args is not None:
        for key, value in ansible_args.items():
            option = f'--{key.replace("_", "-")}'
            if isinstance(value, bool):
                if value:
                    cmd.append(option)
            else:
                cmd.extend([option, str(value)])

    # Add playbook path as the last argument
    cmd.append(playbook_path)

    # Assuming InfraredWorkspace has a 'path' attribute for the working directory
    cwd = ir_workspace.path

    # Execute the command
    process = subprocess.run(cmd, cwd=cwd)
    return process.returncode
