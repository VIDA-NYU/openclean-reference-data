# This file is part of the Data Cleaning Library (openclean).
#
# Copyright (C) 2018-2021 New York University.
#
# openclean is released under the Revised BSD License. See file LICENSE for
# full license details.

"""Dataset from the REST Countries project. Get information about countries via
a RESTful API (https://restcountries.eu/).
"""

import json
import requests
import sys


def download_restcountries(filename: str):
    """Download the data from the restcountries project as a single Json
    document. Writes the retrieved data to disk.

    Raises an error if the download is not successful.

    Parameters
    ----------
    filename: string
        Path to a file on the local disk where the downloaded data is stored
        (as plain Json).
    """
    # Download the full dataset from API endpoint.
    r = requests.get('https://restcountries.eu/rest/v2/all')
    # Raise an error if the download was not successful.
    r.raise_for_status()
    # Write data to disk.
    with open(filename, 'w') as f:
        json.dump(r.json(), f)


if __name__ == '__main__':
    """Download data and write the result to a given file."""
    args = sys.argv[1:]
    # Ensure that the output file parameter is given.
    if len(args) != 1:
        print('usage: {} <output-file>'.format(sys.argv[0]))
        sys.exit(-1)
    # Download data and write to output file.
    download_restcountries(filename=args[0])
