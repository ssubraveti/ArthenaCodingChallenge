import os

from bs4 import BeautifulSoup

import utils

"""
Class that describes an ArtParser object.
"""


class ArtParser:
    def __init__(self, paths):

        # paths is the list of directories where the html files are present
        self.file_paths = paths
        self.soup_objects = self.get_soup_objects()

    def get_soup_objects(self):

        """
        Function that parses the HTML files in the given directory, and converts them into BeautifulSoup objects
        :return:
        soups: List of BeautifulSoup objects
        """
        soups = []
        # For each directory in the list
        for directory in self.file_paths:
            # For each webpage in the directory
            for webpage in os.listdir(directory):
                # If the file is a webpage
                if '.html' in webpage:
                    # Open the file
                    with open(directory + '/' + webpage) as html_file:
                        # Read it as a HTML page, and create a BeautifulSoup object
                        soups.append(BeautifulSoup(html_file, "html.parser"))

        return soups

    def get_div_tags(self):

        """
        Function that returns a list of div tags containing information to be parsed
        :return:
        """
        div_tags = []

        for soup_object in self.soup_objects:
            # Get first div tags of the HTML files
            div_tags.append(soup_object.find_all("div"))

        return div_tags

    def get_artwork_info(self):

        """
        Function that extracts artwork metadata from the BeautifulSoup objects of the files
        :return:
        painter_names: A JSONArray of unique painter names found in the HTML files of the directory.
        """
        painter_data = {}
        prices = {}
        div_tags_list = self.get_div_tags()

        # Extract information for the div tags
        for div_tags in div_tags_list:
            # Content(i.e. artist name and the work) is present in the first div
            content = div_tags[0].contents[0].split("\n")
            # In the first directory, the price is stored directly inside the second div, and hence the length of the
            # contents is 1
            if len(div_tags[1].contents) == 1:
                price = utils.convert_string_to_ascii(div_tags[1].contents[0].strip())
            else:
                # In the second directory, threre are two span tags inside the second div that store this information
                price = utils.convert_string_to_ascii(
                    div_tags[1].contents[0].contents[0]) + " " + utils.convert_string_to_ascii(
                    div_tags[1].contents[1].contents[0])

            # Strip leading and trailing white spaces
            artist = utils.convert_string_to_ascii(content[1].split("(")[0].strip())
            work = utils.convert_string_to_ascii(content[2].strip())

            if artist in painter_data:
                # Avoid duplicate entries for artists across muliple directories
                if work not in prices:
                    painter_data[artist].append(work)
                    prices[work] = price
            else:
                painter_data[artist] = []
                painter_data[artist].append(utils.convert_string_to_ascii(content[2].strip()))
                prices[work] = price
        # Convert dict to JSONArray
        json_array = utils.convert_dict_to_json(painter_data, prices)
        # Return unique names only, and convert the list to a JSONArray
        return json_array
