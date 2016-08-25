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
    try:
        with open(path, 'r') as stream:
            output = yaml.load(stream)

    except IOError:
        output = dict()
    except Exception:
        '''
        I'm using Exception as final exception handling,
        it's because i cannot catch yaml.YAMLError
        '''
        output = dict()

    return output
