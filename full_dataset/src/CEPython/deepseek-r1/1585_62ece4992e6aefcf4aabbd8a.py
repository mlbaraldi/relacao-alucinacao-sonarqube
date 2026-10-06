def load_configurations(config_filenames, overrides=None, resolve_env=True):
    import logging
    """
    Given a sequence of configuration filenames, load and validate each configuration file. Return
    the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
    and sequence of logging.LogRecord instances containing any parse errors.
    """
    configs = {}
    logs = []

    class LogCaptureHandler(logging.Handler):
        def __init__(self, log_list):
            super().__init__()
            self.log_list = log_list

        def emit(self, record):
            self.log_list.append(record)

    logger = logging.getLogger('config_loader')
    original_level = logger.level
    handler = LogCaptureHandler(logs)
    logger.addHandler(handler)
    logger.setLevel(logging.ERROR)

    try:
        for filename in config_filenames:
            try:
                # Load and parse configuration file
                config = parse_config_file(filename)
                
                # Apply overrides
                if overrides is not None:
                    config.update(overrides)
                
                # Resolve environment variables
                if resolve_env:
                    config = resolve_env_vars(config)
                
                # Validate configuration
                validate_config(config)
                
                configs[filename] = config
            except Exception as e:
                logger.error("Error processing configuration file '%s'", filename, exc_info=True)
    finally:
        logger.removeHandler(handler)
        logger.setLevel(original_level)

    return configs, logs
