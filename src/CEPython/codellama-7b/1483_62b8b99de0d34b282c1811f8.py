

def _reset_logging(cls):
    # Clear the logging handlers
    cls.logger.handlers = []

    # Set the logging level to the default value
    cls.logger.setLevel(logging.INFO)

    # Create a new logging handler
    handler = logging.StreamHandler()

    # Set the logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the logging handler to the logger
    cls.logger.addHandler(handler)
