

def on(self, hook):
    def decorator(func):
        self.handlers[hook].append(func)
        return func
    return decorator
