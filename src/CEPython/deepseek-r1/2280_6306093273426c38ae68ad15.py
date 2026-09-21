def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    import subprocess
    import json
    """Runs ansible cli with vars dict

    :param vars_dict: dict, Will be passed as Ansible extra-vars
    :param cli_args: the list of command line arguments
    :param ir_workspace: An Infrared Workspace object represents the active workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :return: ansible results
    """
    # Convert the vars_dict to a JSON string for Ansible extra-vars
    extra_vars = json.dumps(vars_dict)
    
    # Build the command list including ansible-playbook, cli_args, and extra-vars
    command = ['ansible-playbook'] + cli_args + ['--extra-vars', extra_vars]
    
    # Execute the Ansible playbook command and capture the results
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True  # Returns stdout/stderr as strings
    )
    
    return result
