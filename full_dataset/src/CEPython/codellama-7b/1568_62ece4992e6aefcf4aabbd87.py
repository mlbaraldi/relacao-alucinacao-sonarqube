import logging


def build_app_logger(name='app', logfile='app.log', debug=True):
    # Create a logger
    logger = logging.getLogger(name)

    # Set the log level
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Create a file handler
    file_handler = logging.FileHandler(logfile)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add the formatter to the file handler
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Return the logger
    return logger
