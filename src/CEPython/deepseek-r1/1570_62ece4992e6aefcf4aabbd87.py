def build_app_logger(name='app', logfile='app.log', debug=True):
    import logging
    """
    General purpose application logger. Useful mainly for debugging
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # Prevent logs from propagating to the root logger

    # Remove any existing handlers to avoid duplication
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Create and configure the file handler
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Add stream handler with debug formatter if debug is True
    if debug:
        stream_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s'
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

    return logger
