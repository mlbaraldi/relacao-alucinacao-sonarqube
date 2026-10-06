import os
import json
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase


def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Runs ansible cli with vars dict

    :param vars_dict: dict, Will be passed as Ansible extra-vars
    :param cli_args: the list of command line arguments
    :param ir_workspace: An Infrared Workspace object represents the active workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :return: ansible results
    """
    # Initialize Ansible objects
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=InventoryManager(loader=loader, sources='localhost'))

    # Load the playbook file
    playbook_path = ir_workspace.get_playbook_path()  # Assuming this method returns the path to the playbook
