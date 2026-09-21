

def _reset_logging(cls):
    """
    Reset
    """
    # Assuming that the logging mechanism is a list of logs
    if hasattr(cls, 'logs'):
        cls.logs = []
    else:
        print("No logging mechanism found.")
