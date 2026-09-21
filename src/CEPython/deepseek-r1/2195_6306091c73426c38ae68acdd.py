def validate_from_file(cls, yaml_file=None):
    import yaml
    """
    Loads & validates that a YAML file has all required fields

    :param yaml_file: Path to YAML file
    :raise IRValidatorException: when mandatory data is missing in file
    :return: Dictionary with data loaded from a YAML file
    """
    if yaml_file is None:
        raise IRValidatorException("YAML file path is required.")
    
    try:
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError as e:
        raise IRValidatorException(f"File not found: {yaml_file}") from e
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Invalid YAML syntax: {e}") from e
    except IOError as e:
        raise IRValidatorException(f"Error reading file: {e}") from e
    
    if not isinstance(data, dict):
        raise IRValidatorException("YAML content is not a dictionary.")
    
    required_fields = getattr(cls, 'REQUIRED_FIELDS', [])
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        raise IRValidatorException(f"Missing required fields: {', '.join(missing_fields)}")
    
    return data
