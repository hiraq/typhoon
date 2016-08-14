import yaml

def load_yaml_env(path):
    output = ''
    with open(path, 'r') as stream:
        try:
            output = yaml.load(stream)
        except yaml.YAMLERROR as exc:
            output = dict()

    return output
