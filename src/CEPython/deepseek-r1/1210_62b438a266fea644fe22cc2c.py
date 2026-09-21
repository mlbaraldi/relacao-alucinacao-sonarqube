def make_parsers():
    import argparse
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    return (parser, subparsers)
