import yaml


def load_yaml(path):
    """
    Reads a YAML file and converts its contents into a Python datatype.
    """
    with open(path, 'r') as f:
        data = yaml.load(f.read())

    return data
