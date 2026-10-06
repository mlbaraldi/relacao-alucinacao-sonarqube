def deep_merge_nodes(nodes):
    """
    Deep merges a list of nodes, combining values of duplicate keys. If any value is a non-MappingNode,
    the last value for that key is taken. All MappingNode values are merged recursively.
    """
    # Group nodes by their key (ScalarNode's tag and value)
    key_groups = {}
    for key_node, value_node in nodes:
        key = (key_node.tag, key_node.value)
        if key not in key_groups:
            key_groups[key] = []
        key_groups[key].append(value_node)
    
    merged_nodes = []
    for key, value_nodes in key_groups.items():
        # Check if all values are MappingNodes
        all_mapping = all(isinstance(v, MappingNode) for v in value_nodes)
        if all_mapping:
            # Collect all the value lists from each MappingNode
            concatenated = []
            for v in value_nodes:
                concatenated.extend(v.value)
            # Recursively merge the concatenated list of nodes
            merged_value = deep_merge_nodes(concatenated)
            # Create new key and value nodes
            new_key = ScalarNode(tag=key[0], value=key[1])
            # Use the tag from the last MappingNode in the group
            new_value_tag = value_nodes[-1].tag
            new_value = MappingNode(tag=new_value_tag, value=merged_value)
            merged_nodes.append((new_key, new_value))
        else:
            # Take the last value node and create new key node
            new_key = ScalarNode(tag=key[0], value=key[1])
            new_value = value_nodes[-1]
            merged_nodes.append((new_key, new_value))
    
    return merged_nodes
