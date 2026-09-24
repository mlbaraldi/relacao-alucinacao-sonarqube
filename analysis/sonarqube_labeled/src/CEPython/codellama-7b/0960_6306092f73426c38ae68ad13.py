import subprocess


def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None,
                     extra_vars=None, ansible_args=None):
    # Build the ansible-playbook command
    command = ['ansible-playbook', playbook_path]

    # Add the verbose flag if specified
    if verbose:
        command.append('-' + verbose)

    # Add the extra-vars flag if specified
    if extra_vars:
        command.append('--extra-vars')
        command.append(extra_vars)

    # Add the ansible-playbook arguments if specified
    if ansible_args:
        command.extend(ansible_args)

    # Run the ansible-playbook command
    subprocess.run(command, check=True)
