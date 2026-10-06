import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def xml_children_as_dict(node):
    children = node.findall('*')
    result = {}
    for child in children:
        result[child.tag] = child.text
        if child.findall('*'):
            result.update(xml_children_as_dict(child))
    return result
