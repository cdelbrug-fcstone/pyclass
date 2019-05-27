from sys import argv
import yaml

script_name, filename = argv

with open(filename) as file:
    yaml_out = yaml.load(file)
print(yaml_out)
