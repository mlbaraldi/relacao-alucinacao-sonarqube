

def derivative(xs: list):
    if len(xs) == 0:
        return []
    else:
        return [xs[i] * (i + 1) for i in range(len(xs) - 1)]
