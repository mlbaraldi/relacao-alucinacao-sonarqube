import yaml


def validate_from_file(cls, yaml_file=None):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    # Check if all required fields are present
    required_fields = ['name', 'age', 'gender']
    for field in required_fields:
        if field not in data:
            raise IRValidatorException(f'Missing required field: {field}')

    # Check if age is an integer
    if not isinstance(data['age'], int):
        raise IRValidatorException(f'Invalid age: {data["age"]}')

    # Check if gender is one of the allowed values
    if data['gender'] not in ['male', 'female', 'other']:
        raise IRValidatorException(f'Invalid gender: {data["gender"]}')

    return data
