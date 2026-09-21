import yaml


def validate_from_file(cls, yaml_file=None):
    """
    Loads & validates that a YAML file has all required fields

    :param yaml_file: Path to YAML file
    :raise IRValidatorException: when mandatory data is missing in file
    :return: Dictionary with data loaded from a YAML file
    """
    if not yaml_file:
        raise IRValidatorException("YAML file path is required")

    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        raise IRValidatorException(f"YAML file {yaml_file} not found")
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Error loading YAML file {yaml_file}: {str(e)}")

    # Assuming that the mandatory fields are 'field1', 'field2', etc.
    # You can replace these with your actual mandatory fields
    mandatory_fields = ['field1', 'field2', 'field3']

    for field in mandatory_fields:
        if field not in data:
            raise IRValidatorException(f"Mandatory field {field} is missing in YAML file {yaml_file}")

    return data
