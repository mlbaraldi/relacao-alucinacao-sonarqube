import yaml


def validate_from_file(cls, yaml_file=None):
    """
    Loads & validates that a YAML file has all required fields

    :param yaml_file: Path to YAML file
    :raise IRValidatorException: when mandatory data is missing in file
    :return: Dictionary with data loaded from a YAML file
    """
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    for field in self.required_fields:
        if field not in data:
            raise IRValidatorException(f"Missing required field: {field}")

    return data
