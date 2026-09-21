

def status_str(self, prefix=''):
    """
    Return string of validator status, with optional prefix.
    """
    status_str = "Active" if self.status else "Inactive"
    return f"{prefix} {status_str}" if prefix else status_str
