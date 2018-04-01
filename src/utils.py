import json
import unicodedata
# locale.setlocale(locale.LC_ALL, 'en_US.utf8')
from collections import OrderedDict


def convert_gbp_to_usd(gbp):
    """
    Function that converts GBP amounts to USD
    :param gbp:
    :return:
    """
    return gbp * 1.34

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
        total_value = 0
        for work in works:
            work_metadata = OrderedDict()
            # Title of the work
            work_metadata['title'] = work
            # Currency of the price
            work_metadata['currency'] = 'USD'
            # Amount
            price = prices_dict[work].split(" ")

            # If USD, use the direct amount, else convert to USD and insert commas at the right places
            work_metadata['totalLifetimeValue'] = price[1] if price[0] == 'USD' else format(
                convert_gbp_to_usd(float(price[1].replace(',', ''))), ',')

            # Add value of the work to the total amount
            total_value += float(work_metadata['amount'].replace(',', ''))
            work_data.append(work_metadata)
        # Total lifetime value of the artist
        data_dict['totalValue'] = "USD " + format(total_value, ',')
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
