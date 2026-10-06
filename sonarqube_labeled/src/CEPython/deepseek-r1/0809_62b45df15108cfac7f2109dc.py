def status_str(self, prefix=''):
    """
    Return string of validator status, with optional prefix.
    """
    parts = []
    if self.jailed:
        parts.append("Jailed")
    else:
        if self.elected:
            parts.append("Elected")
            if self.active:
                uptime_percent = self.uptime * 100  # Assuming uptime is a float between 0 and 1
                parts.append(f"Active ({uptime_percent:.1f}% uptime)")
            else:
                parts.append("Inactive")
        elif self.pending:
            parts.append("Pending")
        else:
            parts.append("Idle")
    status = ", ".join(parts)
    return f"{prefix}{status}"
