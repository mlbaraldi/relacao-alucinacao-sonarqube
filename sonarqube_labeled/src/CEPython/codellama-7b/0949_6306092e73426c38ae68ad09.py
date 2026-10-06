

def validate_length_args(self, args):
    for arg in args:
        if len(arg) > self.length:
            raise ValueError(f"Argument {arg} is longer than {self.length} characters")
