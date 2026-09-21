

def validate_requires_args(self, args):
    required_args = self.get_required_args()
    for arg in required_args:
        if arg not in args:
            raise ValueError(f"Required argument {arg} not provided")
