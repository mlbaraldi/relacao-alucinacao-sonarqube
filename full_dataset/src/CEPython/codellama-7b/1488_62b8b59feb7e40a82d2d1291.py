

def _getTargetClass(self):
    if self.implementation == 'Py':
        return self.implementation
    elif self.implementation == 'Fallback':
        return self.implementation
    else:
        raise ValueError('Invalid implementation: {}'.format(self.implementation))
