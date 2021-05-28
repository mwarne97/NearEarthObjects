"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from models import NearEarthObject, CloseApproach
from pathlib import Path


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    filename = Path(neo_csv_path)
    filename.resolve()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        neo_list = []
        for container in reader:
            if container['pha'] == 'Y':
                hazardous = True
            else:
                hazardous = False
            neo = NearEarthObject(des=container['pdes'], name=container['name'], dia=container['diameter'],
                                  haz=hazardous)
            neo_list.append(neo)
    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    filename = Path(cad_json_path)
    filename.resolve()
    with open(filename, 'r') as file:
        reader_json = json.load(file)
        close_approach_list = []
        for container in reader_json['data']:
            ca = CloseApproach(des=container[0], time=container[3], dis=container[4], vel=container[7])
            close_approach_list.append(ca)
    return close_approach_list
