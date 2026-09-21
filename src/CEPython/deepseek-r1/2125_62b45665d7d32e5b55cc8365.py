def parse_arguments(*unparsed_arguments):
    import argparse
    # Create the main parser for global arguments
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('--global-arg', help='Global argument (example)')
    
    # Add subparsers for commands
    subparsers = main_parser.add_subparsers(
        title='subcommands',
        dest='command',
        required=True
    )
    
    # Example subparser for command 'a'
    parser_a = subparsers.add_parser('a')
    parser_a.add_argument('--foo', required=True, help='foo help for a')
    
    # Example subparser for command 'b'
    parser_b = subparsers.add_parser('b')
    parser_b.add_argument('--bar', type=int, help='bar help for b')
    
    # Parse all arguments using the main parser
    parsed_args = main_parser.parse_args(unparsed_arguments)
    
    # Determine the subcommand used
    command = parsed_args.command
    
    # Collect destinations for main parser and subparser
    global_dests = {action.dest for action in main_parser._actions if action.dest != argparse.SUPPRESS}
    subparser = subparsers.choices[command]
    command_dests = {action.dest for action in subparser._actions if action.dest != argparse.SUPPRESS}
    
    # Split the arguments into global and command-specific
    global_args = {}
    command_args = {}
    for key, value in vars(parsed_args).items():
        if key in global_dests:
            global_args[key] = value
        if key in command_dests:
            command_args[key] = value
    
    # Create Namespace objects
    global_namespace = argparse.Namespace(**global_args)
    command_namespace = argparse.Namespace(**command_args)
    
    return {'global': global_namespace, command: command_namespace}
