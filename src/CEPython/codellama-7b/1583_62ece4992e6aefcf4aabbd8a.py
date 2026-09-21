import logging
import os


def load_configurations(config_filenames, overrides=None, resolve_env=True):
    configs = {}
    errors = []

    for config_filename in config_filenames:
        config = {}
        with open(config_filename, 'r') as f:
            try:
                config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                errors.append(logging.LogRecord(logging.ERROR, 'Error parsing configuration file: %s', config_filename))
                continue

        if overrides:
            config.update(overrides)

        if resolve_env:
            config = resolve_env_vars(config)

        configs[config_filename] = config

    return configs, errors
