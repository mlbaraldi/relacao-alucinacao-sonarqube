from collections import defaultdict
from ruamel.yaml.nodes import ScalarNode, MappingNode


def deep_merge_nodes(nodes):
    merged_nodes = defaultdict(list)
    
    for key, value in nodes:
        if isinstance(value, MappingNode):
            # If the value is a MappingNode, we need to merge its contents
            for subkey, subvalue in value.value:
                merged_nodes[(key, subkey)].append(subvalue)
        else:
            # If the value is not a MappingNode, we can simply append it to the list
            merged_nodes[key].append(value)
    
    # Now we need to combine the merged nodes into the final result
    result = []
    for key, values in merged_nodes.items():
        if isinstance(key, tuple) and isinstance(values[0], MappingNode):
            # If the key is a tuple and the values are MappingNodes, we need to merge them
            merged_value = MappingNode(tag='tag:yaml.org,2002:map', value=[])
            for subkey, subvalue in zip(values[0].value[0], values):
                merged_value.value.append((subkey, subvalue))
            result.append((key[0], merged_value))
        else:
            # Otherwise, we can simply take the last value
            result.append((key, values[-1]))
    
    return result

# Example usage:
