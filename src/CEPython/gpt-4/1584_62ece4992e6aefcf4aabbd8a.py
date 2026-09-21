import json
import os
import logging


def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Given a sequence of configuration filenames, load and validate each configuration file. Return
    the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
    and sequence of logging.LogRecord instances containing any parse errors.
    """
    configs = {}
    log_records = []

    for filename in config_filenames:
        try:
            with open(filename, 'r') as f:
                config = json.load(f)

                # Apply overrides if any
                if overrides:
                    config.update(overrides)

                # Resolve environment variables if required
                if resolve_env:
                    for key, value in config.items():
                        if isinstance(value, str) and value.startswith('$'):
                            config[key] = os.getenv(value[1:])

                configs[filename] = config

        except json.JSONDecodeError as e:
            log_record = logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=e.doc,
                msg=str(e),
                args=None,
                exc_info=None
            )
            log_records.append(log_record)

    return configs, log_records
