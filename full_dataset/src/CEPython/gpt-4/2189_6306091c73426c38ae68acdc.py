import yaml


def validate_from_content(cls, spec_content=None):
    """
    validates that spec (YAML) content has all required fields

    :param spec_content: content of spec file
    :raise IRValidatorException: when mandatory data
    is missing in spec file
    :return: Dictionary with data loaded from a spec (YAML) file
    """
    if spec_content is None:
        raise IRValidatorException("Spec content is missing")

    try:
        data = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException("Invalid YAML content") from e

    required_fields = ["field1", "field2", "field3"]  # replace with your actual required fields

    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise IRValidatorException(f"Missing required fields: {', '.join(missing_fields)}")

    return data
