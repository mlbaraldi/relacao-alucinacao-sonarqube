def validate_from_content(cls, spec_content=None):
    import yaml
    """
    Validates that spec (YAML) content has all required fields.

    :param spec_content: content of spec file
    :raise IRValidatorException: when mandatory data is missing in spec file
    :return: Dictionary with data loaded from a spec (YAML) file
    """
    try:
        # Load YAML content, handle None as empty content
        data = yaml.safe_load(spec_content) if spec_content is not None else None
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Invalid YAML content: {e}")

    # Ensure data is a dictionary
    if not isinstance(data, dict):
        raise IRValidatorException("Spec content must be a dictionary")

    # Check for required fields
    required_fields = cls.REQUIRED_FIELDS
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise IRValidatorException(f"Missing mandatory fields: {', '.join(missing_fields)}")

    return data
