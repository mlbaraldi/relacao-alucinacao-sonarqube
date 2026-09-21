def parse_arguments(*unparsed_arguments):
    import argparse
    # Create the main parser with global arguments
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('--global-arg', help='Global argument')
    subparsers = main_parser.add_subparsers(dest='command', help='Available sub-commands')
    
    # Example subparser 'foo'
    foo_parser = subparsers.add_parser('foo')
    foo_parser.add_argument('--bar', help='Bar argument for foo')
    
    # Example subparser 'baz'
    baz_parser = subparsers.add_parser('baz')
    baz_parser.add_argument('--qux', help='Qux argument for baz')
    
    # Parse all arguments using the main parser
    args = main_parser.parse_args(unparsed_arguments)
    
    result = {}
    global_namespace = {}
    
    # Extract global arguments (excluding 'command')
    for action in main_parser._actions:
        if action.dest == 'command':
            continue
        if hasattr(args, action.dest):
            global_namespace[action.dest] = getattr(args, action.dest)
    
    result['global'] = argparse.Namespace(**global_namespace)
    
    # Extract subparser arguments if a command was provided
    command = getattr(args, 'command', None)
    if command:
        subparser = subparsers.choices[command]
        sub_namespace = {}
        for action in subparser._actions:
            if hasattr(args, action.dest):
                sub_namespace[action.dest] = getattr(args, action.dest)
        result[command] = argparse.Namespace(**sub_namespace)
    
    return result
