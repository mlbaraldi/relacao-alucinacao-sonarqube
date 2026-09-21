import ruamel.yaml


def deep_merge_nodes(nodes):
    result = []
    for node in nodes:
        key, value = node
        if key.tag == 'tag:yaml.org,2002:str':
            result.append((key, value))
        elif key.tag == 'tag:yaml.org,2002:map':
            result.append((key, deep_merge_nodes(value)))
        else:
            raise ValueError(f"Unsupported key type: {key.tag}")
    return result
