

def create_complex_argumet_type(self, subcommand, type_name, option_name,
                                    spec_option):
Sure, here is a simple implementation of the function. Please note that the actual implementation may vary depending on the context and the specific requirements of your project.

```python
class MyProgram:
    def __init__(self):
        self.commands = {}

    def create_complex_argument_type(self, subcommand, type_name, option_name, spec_option):
        """
        Build the complex argument type

        :param subcommand: the command name
        :param type_name: the complex type name
        :param option_name: the option name
        :param spec_option: option's specifications
        :return: the complex type instance
        """
        if subcommand not in self.commands:
            self.commands[subcommand] = {}

        if type_name not in self.commands[subcommand]:
            self.commands[subcommand][type_name] = {}

        self.commands[subcommand][type_name][option_name] = spec_option

        return self.commands[subcommand][type_name]
