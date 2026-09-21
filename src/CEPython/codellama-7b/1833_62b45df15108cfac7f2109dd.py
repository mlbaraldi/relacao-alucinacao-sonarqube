

def status_str(self, prefix=''):
    status_str = ''
    for key, value in self.validation_log.items():
        status_str += f'{prefix}{key}: {value}\n'
    return status_str
