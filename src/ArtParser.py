import json
import os
import unicodedata

from bs4 import BeautifulSoup

"""
Class that describes an ArtParser object.
"""


class ArtParser:
    def __init__(self, path):

        # path is the directory where the html files are present
        self.file_path = path
        self.soup_objects = self.get_soup_objects()

    def get_soup_objects(self):

        """
        Function that parses the HTML files in the given directory, and converts them into BeautifulSoup objects
        :return:
        soups: List of BeautifulSoup objects
        """
        soups = []
        for webpage in os.listdir(self.file_path):
            # If the file is a webpage
            if '.html' in webpage:
                # Open the file
                with open(self.file_path + '/' + webpage) as html_file:
                    # Read it as a HTML page, and create a BeautifulSoup object
                    soups.append(BeautifulSoup(html_file, "html.parser"))

        return soups

    def get_painter_names(self):

        """
        Function that extracts painter names from the BeautifulSoup objects of the files
        :return:
        painter_names: A JSONArray of unique painter names found in the HTML files of the directory.
        """
        painter_names = []

        for soup_object in self.soup_objects:
            # Extract information from the first div tag
            div_tag = soup_object.find("div").contents[0].split("\n")
            # Strip leading and trailing white spaces
            name = div_tag[1].split("(")[0].strip()
            # Convert from unicode to ascii. Convert accented characters to normal form.
            painter_names.append(unicodedata.normalize("NFKD", name).encode("ascii", "ignore"))
        # Return unique names only, and convert the list to a JSONArray
        return json.dumps(list(set(painter_names)))
