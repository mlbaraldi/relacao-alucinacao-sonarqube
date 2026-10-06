

def bash_completion():
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='store_true', help='Show this help message and exit')
    parser.add_argument('--version', action='store_true', help='Show the version number and exit')
    parser.add_argument('--list', action='store_true', help='List all available commands')
    parser.add_argument('--command', action='store', help='Run a specific command')
    parser.add_argument('--option', action='store', help='Set an option for the command')

    # Introspect the command-line argument parsers to generate the bash completion script
    for action in parser._actions:
        if action.option_strings:
            for option in action.option_strings:
                print(f'complete -F _borgmatic_completion {option}')

    # Define the _borgmatic_completion function
    def _borgmatic_completion(text, state):
        options = []
        for action in parser._actions:
            if action.option_strings:
                for option in action.option_strings:
                    if option.startswith(text):
                        options.append(option)
        return options[state]

    # Print the bash completion script
    print('_borgmatic_completion() {')
    print('    local cur prev')
    print('    COMPREPLY=()')
    print('    cur="${COMP_WORDS[COMP_CWORD]}"')
    print('    prev="${COMP_WORDS[COMP_CWORD-1]}"')
    print('    case "$prev" in')
    print('        --command)')
    print('            COMPREPLY=($(compgen -W "$(borgmatic --list)" -- "$cur"))')
    print('            ;;')
