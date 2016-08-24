import yaml

def load_yaml_env(path):
    """Load YAML Variables

    Used to read yml files and load all key value
    variables.

    Args:
        path (string) : A full path to yaml file

    Returns:
        A dictionary contains of all yaml key values
    """
    output = ''
    with open(path, 'r') as stream:
        try:
            output = yaml.load(stream)
        except yaml.YAMLERROR as exc:
            output = dict()

    return output
