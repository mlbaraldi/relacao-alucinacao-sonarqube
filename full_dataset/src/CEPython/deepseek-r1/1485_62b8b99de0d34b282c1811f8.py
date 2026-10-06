def _reset_logging(cls):
    import logging
    """
    Reset the logging configuration by removing all handlers from the root logger
    and resetting its level to NOTSET.
    """
    root = logging.getLogger()
    for handler in root.handlers[:]:
        root.removeHandler(handler)
        handler.close()
    root.setLevel(logging.NOTSET)
