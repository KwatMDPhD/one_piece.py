from json import dump, load


def read(json_file_path):

    with open(json_file_path) as io:

        return load(io)


def write(json_file_path, dict_, indent=2):

    with open(json_file_path, mode="w") as io:

        dump(dict_, io, indent=indent)