import argparse
import shlex


def bash_completion():
    """
    Return a bash completion script for the borgmatic command. Produce this by introspecting
    borgmatic's command-line argument parsers.
    """
    # Assuming we have a function get_borgmatic_parser() that returns the argument parser for borgmatic
    parser = get_borgmatic_parser()

    commands = parser._subparsers._group_actions[0].choices.keys()

    bash_script = """
_borgmatic_completions()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="{}"

    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}
complete -F _borgmatic_completions borgmatic
""".format(' '.join(commands))

    return bash_script
