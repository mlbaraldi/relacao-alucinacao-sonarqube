import yaml
from marshmallow_yaml import YamlSchema
from marshmallow import ValidationError


def validate_from_content(cls, spec_content=None):
    """
    validates that spec (YAML) content has all required fields

    :param spec_content: content of spec file
    :raise IRValidatorException: when mandatory data
    is missing in spec file
    :return: Dictionary with data loaded from a spec (YAML) file
    """
    schema = YamlSchema()
    try:
        data = schema.loads(spec_content)
    except ValidationError as e:
        raise IRValidatorException('Invalid YAML content') from e
    return data
