

def on(self, hook):
    def decorator(func):
        if hook not in self._hooks:
            self._hooks[hook] = []
        self._hooks[hook].append(func)
        return func
    return decorator
