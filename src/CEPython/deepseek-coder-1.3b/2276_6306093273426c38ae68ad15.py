import subprocess


def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Runs ansible cli with vars dict

    :param vars_dict: dict, Will be passed as Ansible extra-vars
    :param cli_args: the list  of command line arguments
    :param ir_workspace: An Infrared Workspace object represents the active
    workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :return: ansible results
    """

    # Construct the command line arguments
    cmd = ['ansible-playbook'] + cli_args

    # Add the extra vars
    cmd += ['-e', '{}={}'.format(k, v) for k, v in vars_dict.items()]

    # Run the command and capture the output
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Return the results
    return {'stdout': stdout.decode(), 'stderr': stderr.decode()}
