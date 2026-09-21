import configparser
import logging


def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Given a sequence of configuration filenames, load and validate each configuration file. Return
    the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
    and sequence of logging.LogRecord instances containing any parse errors.
    """
    configs = {}
    errors = []

    for filename in config_filenames:
        try:
            config = configparser.ConfigParser()
            config.read(filename)

            if overrides:
                config.update(overrides)

            if resolve_env:
                config.optionxform = str  # transform all keys to lower case

            configs[filename] = config
        except Exception as e:
            errors.append(logging.LogRecord(name='configparser', level=logging.ERROR,
                                            message=f'Error parsing {filename}: {str(e)}'))

    return configs, errors
