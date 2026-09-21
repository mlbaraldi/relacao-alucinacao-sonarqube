

def get_silent_args(self, args):
    silent_args = []
    for arg in args:
        if arg.startswith('-'):
            silent_args.append(arg)
    return silent_args
