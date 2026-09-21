

def validate_choices_args(self, args):
    for arg in args:
        if arg not in self.choices:
            raise ValueError(f"Invalid choice: {arg}. Must be one of {self.choices}")
