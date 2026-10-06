import subprocess


def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    # Convert vars_dict to a string in the format: key1=value1 key2=value2 ...
    extra_vars = ' '.join(['{}={}'.format(k, v) for k, v in vars_dict.items()])

    # Get the paths for the workspace and plugin
    workspace_path = ir_workspace.get_path()
    plugin_path = ir_plugin.get_path()

    # Construct the ansible-playbook command
    cmd = ['ansible-playbook', '-i', workspace_path, '-e', extra_vars, plugin_path] + cli_args

    # Run the command and capture the output
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # If the command failed, raise an exception
    if process.returncode != 0:
        raise Exception('ansible-playbook command failed: {}'.format(stderr))

    # Return the command output
    return stdout
