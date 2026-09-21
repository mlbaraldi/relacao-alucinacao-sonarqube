import yaml
import jsonschema
from jsonschema import validate


def validate_from_file(cls, yaml_file=None):
    """
    Loads & validates that a YAML file has all required fields

    :param yaml_file: Path to YAML file
    :raise IRValidatorException: when mandatory data is missing in file
    :return: Dictionary with data loaded from a YAML file
    """
    if yaml_file is None:
        raise IRValidatorException("No file provided")

    with open(yaml_file, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise IRValidatorException("Error loading YAML file") from exc

    try:
        validate(instance=data, schema=cls.schema)
    except jsonschema.exceptions.ValidationError as exc:
        raise IRValidatorException("Mandatory data is missing in file") from exc

    return data
