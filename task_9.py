import json
import yaml
import xml.etree.ElementTree as ET
from functools import wraps


def to_json(data):
    """
    Converts a Python data structure to a formatted JSON string.

    Args:
        data (any): The data to convert, typically a dict, list, etc.

    Returns:
        str: A JSON-formatted string with indentation for readability,
             and Unicode characters properly encoded.
    """
    return json.dumps(data, ensure_ascii=False, indent=2)


def to_xml(data, root_name="root"):
    """
    Converts a Python data structure to an XML string.

    Args:
        data (dict, list, or other): The data to convert into XML format.
        root_name (str): The name of the root element in the resulting XML.
                          Defaults to 'root'.

    Returns:
        str: A string in XML format representing the input data.
    """

    def build(parent, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                child = ET.SubElement(parent, key)
                build(child, value)
        elif isinstance(obj, list):
            for item in obj:
                child = ET.SubElement(parent, "item")
                build(child, item)
        else:
            parent.text = str(obj)

    root = ET.Element(root_name)
    build(root, data)
    return ET.tostring(root, encoding="unicode", method="xml")


def to_yaml(data):
    """
    Converts a Python data structure to a YAML-formatted string.

    Args:
        data (any): The data to convert, usually a dict, list, etc.

    Returns:
        str: A string in YAML format, with Unicode characters properly encoded,
             and using block style layout for readability.
    """
    return yaml.dump(data, allow_unicode=True, default_flow_style=False, indent=2)


def format(format_type=None):
    """
    Decorator to automatically format the output of a function into JSON, XML, or YAML.

    Args:
        format_type (str, optional): Specifies the format to which the function's
                                     return value should be converted.
                                     Accepts 'json' (default), 'xml', or 'yaml'.
                                     Case-insensitive.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if format_type is None or format_type.lower() == 'json':
                return to_json(result)
            elif format_type.lower() == 'xml':
                return to_xml(result)
            elif format_type.lower() == 'yaml':
                return to_yaml(result)
            else:
                raise ValueError(f"Unsupported format: {format_type}")

        return wrapper

    return decorator


@format()
def get_person():
    return  {
        "name": "Кристина",
        "age": 19,
        "city": ["Благовещенск", "Новосибирск"],
        "sport": "плавание",
        "sport category": "КМС"

    }
print(get_person())

@format("xml")
def get_user():
    return  {
        "users_1": [
            {"id": 21937, "name": "Семём"},
            {"id": 17263, "name": "Аркадий"}
        ],
        "add_id":
            { "id_1": 26337,
             "id_2": 17373 }

           }
print(get_user())

@format('yaml')
def get_student():
    return {
        "name": "Clara",
        "age": 28,
        "hobbies": ["painting", "hiking"]
    }

print(get_student())
