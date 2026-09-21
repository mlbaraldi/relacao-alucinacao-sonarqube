from ruamel.yaml import YAML


def deep_merge_nodes(nodes):
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)

    merged = {}
    for key, value in nodes:
        if key in merged:
            if isinstance(merged[key], list):
                merged[key].append(value)
            else:
                merged[key] = [merged[key], value]
        else:
            merged[key] = value

    return [(k, yaml.represent_mapping(tag=k.tag, mapping=v)) for k, v in merged.items()]
