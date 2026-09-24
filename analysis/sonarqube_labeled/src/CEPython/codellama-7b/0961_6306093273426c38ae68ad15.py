import subprocess


def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    # Create a list of command line arguments
    args = ["ansible-playbook"]
    args.extend(cli_args)

    # Add the vars dict as extra-vars
    args.append("--extra-vars")
    args.append(vars_dict)

    # Run the ansible-playbook command
    result = subprocess.run(args, capture_output=True)

    # Return the ansible results
    return result.stdout.decode("utf-8")
