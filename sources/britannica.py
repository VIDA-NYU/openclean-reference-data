# This file is part of the Data Cleaning Library (openclean).
#
# Copyright (C) 2018-2021 New York University.
#
# openclean is released under the Revised BSD License. See file LICENSE for
# full license details.

"""Datasets that are extracted from web pages of the Encyclopaedia Britannica."""

from html.parser import HTMLParser
from typing import List, Set, Tuple

import csv
import requests
import sys


"""URL for the Encyclopaedia Britannica US Cities Web page."""
URL_US_CITIES = 'https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068'


# -- Helper classes -----------------------------------------------------------

class USCitiesHTMLParser(HTMLParser):
    """Parser for the Encyclopaedia Britannica US Cities Web page. The parser
    extracts names of cities in the US from the web page together with the
    name of the state they appear in.
    """
    def __init__(self):
        """Initialize parser state that keeps track of the document tree and
        the collected results.
        """
        # Make sure to call the constructor of the super class.
        super(USCitiesHTMLParser, self).__init__()
        # States are identified by the following tad sequence:
        # <h2 class="h1"><a.
        self.states = None
        self._open_state = False
        # Lists of city names are identified by:
        # <ul class="topic-list">
        self._reading_cities = False

    def handle_endtag(self, tag: str):
        """Check for closing ul tags to stop accumulating city names for a
        state.
        """
        if tag == 'ul':
            self._reading_cities = False

    def handle_data(self, data):
        """Handle next data element."""
        if self._open_state == 1:
            self.states.append((data.strip(), set()))
            self._open_state = False
        elif self._reading_cities:
            self.states[-1][1].add(data.strip())

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str]]):
        """Handle next start tag in the HTML document."""
        # States are identified by <h2 class="h1"> followed by <a>
        if tag == 'h2':
            if ('class', 'h1') in attrs:
                self._open_state = True
        elif tag == 'a' and self._open_state:
            pass
        elif tag == 'ul' and ('class', 'topic-list') in attrs:
            self._reading_cities = True
        else:
            self._open_state = False

    def download_and_parse(self) -> List[Tuple[str, Set]]:
        """Download and parse of the web site. Returns a list of tuples with
        states and their city names.

        Returns
        -------
        list of tuple of string and set
        """
        # Parse the web page to get al list of US states and their cities.
        r = requests.get(URL_US_CITIES)
        r.raise_for_status()
        self.states = list()
        self.feed(r.text)
        return self.states


def download_uscities(filename: str):
    """Write the dataset containing US city names to the given file. The output
    file format is a tab-delimited csv file with the column header as the first
    line.

    Parameters
    ----------
    filename: string
        Path to output file on disk.
    """
    # Write data to tab-delimited csv file.
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['city', 'state'])
        for state, cities in USCitiesHTMLParser().download_and_parse():
            for city in cities:
                writer.writerow([city, state])


if __name__ == '__main__':
    """Download data and write the result to a given file."""
    args = sys.argv[1:]
    # Ensure that the output file parameter is given.
    if len(args) != 1:
        print('usage: {} <output-file>'.format(sys.argv[0]))
        sys.exit(-1)
    # Download data and write to output file.
    download_uscities(filename=args[0])
