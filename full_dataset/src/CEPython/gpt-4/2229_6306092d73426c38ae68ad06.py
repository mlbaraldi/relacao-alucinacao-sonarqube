

def get_silent_args(self, args):
    silent_args = []
    for arg in args:
        if arg.startswith('--silent-'):
            silent_args.append(arg.replace('--silent-', ''))
    return silent_args
