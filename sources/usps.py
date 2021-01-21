# This file is part of the Data Cleaning Library (openclean).
#
# Copyright (C) 2018-2021 New York University.
#
# openclean is released under the Revised BSD License. See file LICENSE for
# full license details.

"""Datasets that are extracted from web pages of the U.S. Postal Services."""

import csv
import sys


def transform_street_abbrevs(infile: str, outfile: str):
    """Transform the scraped list of Street Suffix Abbreviations from the USPS
    web site https://pe.usps.com/text/pub28/28apc_002.htm into a csv file
    without empty cells.

    Parameters
    ----------
    infile: string
        Path to input file containing the data that was parsed from the web
        site.
    outfile: string
        Path to outfile with transformed data.
    """
    with open(infile, 'r') as fin:
        # Open csv reader for the input file and skip the file header.
        reader = csv.reader(fin)
        next(reader)
        with open(outfile, 'w') as fout:
            # Open output file and write the transformed data.
            writer = csv.writer(fout)
            writer.writerow(['primary_suffix', 'common_suffix', 'standard_suffix'])
            prim_suffix = None
            stnd_suffix = None
            for row in reader:
                if row[0]:
                    prim_suffix = row[0]
                if row[2]:
                    stnd_suffix = row[2]
                writer.writerow([prim_suffix, row[1], stnd_suffix])


if __name__ == '__main__':
    """Transform data and write the result to a given file. Currently supports
    transformation for the following data:

    - street_abbrevs: C1 Street Suffix Abbreviations
    """
    args = sys.argv[1:]
    # Ensure that the input and output file parameters is given.
    if len(args) != 3:
        print('usage: {} <type> <input-file> <output-file>'.format(sys.argv[0]))
        sys.exit(-1)
    # Call transformer depending on type identifier.
    input_type = args[0]
    if input_type == 'street_abbrevs':
        # Transform data and write to output file.
        transform_street_abbrevs(infile=args[1], outfile=args[2])
    else:
        raise ValueError("unknown type '{}'".format(input_type))
