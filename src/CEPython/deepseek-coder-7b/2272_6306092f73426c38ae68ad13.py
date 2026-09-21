import subprocess
import json


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
    # Construct the command
    command = ['ansible-playbook', playbook_path]

    # Add verbose argument if provided
    if verbose is not None:
        command.extend(['-v'] * verbose)

    # Add extra vars if provided
    if extra_vars is not None:
        for key, value in extra_vars.items():
            command.extend(['--extra-vars', f'{key}={value}'])

    # Add ansible args if provided
    if ansible_args is not None:
        for key, value in ansible_args.items():
            command.extend([f'--{key}', json.dumps(value)])

    # Call the command
    subprocess.run(command, check=True)
