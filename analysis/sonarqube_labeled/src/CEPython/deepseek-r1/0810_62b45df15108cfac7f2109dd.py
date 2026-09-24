def status_str(self, prefix=''):
    """
    Return string representation of validation log, with optional prefix.
    """
    return '\n'.join(
        f"{prefix}{entry.status.capitalize()}: {entry.message}"
        for entry in self._log
    )
