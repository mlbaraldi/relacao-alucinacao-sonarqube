import subprocess


def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None,
                     extra_vars=None, ansible_args=None):
    """
    Wraps the 'ansible-playbook' CLI.

    :param ir_workspace: An Infrared Workspace object represents the active
    workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :param playbook_path: the playbook to invoke
    :param verbose: Ansible verbosity level
    :param extra_vars: dict. Passed to Ansible as extra-vars
    :param ansible_args: dict of ansible-playbook arguments to plumb down
    directly to Ansible.
    """

    # Construct the command line arguments
    command = ['ansible-playbook']

    if verbose is not None:
        command.append('-v' if verbose else '-vv')

    if extra_vars is not None:
        command.append('--extra-vars')
        command.append(' '.join(f'{k}={v}' for k, v in extra_vars.items()))

    if ansible_args is not None:
        command.append('--')
        command.append(' '.join(f'{k}={v}' for k, v in ansible_args.items()))

    command.append(playbook_path)

    # Run the command
    subprocess.run(command, cwd=ir_workspace.path)
