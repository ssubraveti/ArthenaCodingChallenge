import json
import unicodedata
from collections import OrderedDict


def convert_dict_to_json(painter_dict, prices_dict):
    """
    Convert a dictionary of metadata information into a JSONArray
    :param painter_dict: Dictionary of metadata
    :param prices_dict: Dictionary of prices
    :return:
    json_array: A string form of the JSON array
    """
    final_array = []

    for artist, works in painter_dict.iteritems():
        data_dict = OrderedDict()
        data_dict['artist'] = artist
        work_data = []
        # Store prices for each work by the artist
        for work in works:
            work_metadata = OrderedDict()
            # Title of the work
            work_metadata['title'] = work
            # Currency of the price
            work_metadata['currency'] = prices_dict[work].split(" ")[0]
            # Amount
            work_metadata['amount'] = prices_dict[work].split(" ")[1]
            work_data.append(work_metadata)
        # Works by the artist
        data_dict['works'] = work_data
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
