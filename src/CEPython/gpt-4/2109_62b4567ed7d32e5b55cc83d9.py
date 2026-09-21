from ruamel.yaml.nodes import MappingNode, ScalarNode


def deep_merge_nodes(nodes):
    merged = {}
    for key_node, value_node in nodes:
        key = key_node.value
        if key in merged:
            if isinstance(value_node, MappingNode):
                merged[key].value = deep_merge_nodes(merged[key].value + value_node.value)
            else:
                merged[key] = value_node
        else:
            merged[key] = value_node
    return [
        (ScalarNode(tag='tag:yaml.org,2002:str', value=key), value)
        for key, value in merged.items()
    ]
