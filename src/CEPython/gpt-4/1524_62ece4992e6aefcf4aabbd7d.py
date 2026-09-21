import subprocess
import os
import importlib
import pickle
import base64


def subprocess_run_helper(func, *args, timeout, extra_env=None):
    # Get the module and function name
    module_name = func.__module__
    func_name = func.__name__

    # Serialize the arguments
    serialized_args = base64.b64encode(pickle.dumps(args)).decode()

    # Prepare the command
    command = f'python -c "import base64, pickle, {module_name}; ' \
              f'args = pickle.loads(base64.b64decode(\'{serialized_args}\')); ' \
              f'{module_name}.{func_name}(*args)"'

    # Prepare the environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Run the subprocess
    result = subprocess.run(command, shell=True, timeout=timeout, env=env)

    return result
