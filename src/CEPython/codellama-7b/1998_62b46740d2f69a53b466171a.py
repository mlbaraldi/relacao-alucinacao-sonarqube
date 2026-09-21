

def pretty(self, indent=0, debug=False):
    if debug:
        print(f"{indent * ' '}{self.value}")
    if self.left:
        self.left.pretty(indent + 1, debug)
    if self.right:
        self.right.pretty(indent + 1, debug)
