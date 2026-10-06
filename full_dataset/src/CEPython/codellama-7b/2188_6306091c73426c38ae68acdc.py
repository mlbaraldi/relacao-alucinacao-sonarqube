import yaml


def validate_from_content(cls, spec_content=None):
    try:
        spec = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Error parsing YAML: {e}")

    # Check for mandatory fields
    if "name" not in spec:
        raise IRValidatorException("'name' field is missing in spec")
    if "version" not in spec:
        raise IRValidatorException("'version' field is missing in spec")
    if "description" not in spec:
        raise IRValidatorException("'description' field is missing in spec")

    # Check for optional fields
    if "author" in spec:
        if not isinstance(spec["author"], str):
            raise IRValidatorException("'author' field must be a string")
    if "license" in spec:
        if not isinstance(spec["license"], str):
            raise IRValidatorException("'license' field must be a string")
    if "dependencies" in spec:
        if not isinstance(spec["dependencies"], list):
            raise IRValidatorException("'dependencies' field must be a list")

    return spec
