import json
import unicodedata
from collections import OrderedDict


def convert_dict_to_json(input_dict):
    """
    Convert a dictionary of metadata information into a JSONArray
    :param input_dict: Dictionary of metadata
    :return:

    """
    final_array = []

    for key, value in input_dict.iteritems():
        data_dict = OrderedDict()
        data_dict['artist'] = key
        data_dict['works'] = value

        final_array.append(data_dict)

    return json.dumps(final_array, indent=4)


def convert_string_to_ascii(input_str):
    """
    Takes in a unicode encoded string, and converts it into ASCII. Converts accented characters into normal form
    :param input_str: Unicode encoded input string
    :return:
    ascii_str: Converted ASCII string
    """
    return unicodedata.normalize("NFKD", input_str).encode("ascii", "ignore")
