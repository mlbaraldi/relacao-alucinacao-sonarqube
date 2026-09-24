import json
import os
import logging


def load_configurations(config_filenames, overrides=None, resolve_env=True):
    config_dict = {}
    error_log = []

    for filename in config_filenames:
        try:
            with open(filename, 'r') as f:
                config = json.load(f)
                if resolve_env:
                    config = resolve_environment_variables(config)
                if overrides:
                    config.update(overrides)
                config_dict[filename] = config
        except json.JSONDecodeError as e:
            error_log.append(logging.LogRecord(name=None, level=logging.ERROR, pathname=filename, lineno=None, msg=str(e), args=None, exc_info=None))

    return config_dict, error_log
