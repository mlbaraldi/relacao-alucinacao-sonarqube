def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import MappingNode, ScalarNode
    def merge_two_values(a, b):
        if isinstance(a, MappingNode) and isinstance(b, MappingNode):
            merged_children = deep_merge_nodes(a.value + b.value)
            return MappingNode(tag=b.tag, value=merged_children)
        else:
            return b

    grouped = {}
    for key_node, value_node in nodes:
        key = (key_node.tag, key_node.value)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append((key_node, value_node))

    merged_nodes = []
    for group in grouped.values():
        key_nodes = [kn for kn, vn in group]
        value_nodes = [vn for kn, vn in group]

        merged_value = value_nodes[0]
        for vn in value_nodes[1:]:
            merged_value = merge_two_values(merged_value, vn)

        merged_key_node = key_nodes[0]
        merged_nodes.append((merged_key_node, merged_value))

    return merged_nodes
