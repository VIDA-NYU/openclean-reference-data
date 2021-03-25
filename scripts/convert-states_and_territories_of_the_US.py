# This file is part of the Data Cleaning Library (openclean).
#
# Copyright (C) 2018-2021 New York University.
#
# openclean is released under the Revised BSD License. See file LICENSE for
# full license details.

"""Helper functin to parse the U.S. states listing copy-and-pasted from the
Wikiedia page https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States
into a csv file format for publishing.
"""

import csv
import sys

from openclean.function.value.datatype import to_datetime


if __name__ == '__main__':
    """Expects two command line arguments: (1) the input file and (2) the output
    file path.
    """
    args = sys.argv[1:]
    if len(args) != 2:
        print('usage: <input-file> <output-file>')
        sys.exit(-1)
    input_file = args[0]
    output_file = args[1]
    # Parse input file. Columns are assumed to be separated by TAB. Each row is
    # expected to contain 12 or 13 columns. Lines with 12 columns represent states
    # where the largest city is as well the capital.
    headers = [
        'name',
        'postal_abbreviation',
        'capital_city',
        'largest_city',
        'ratification_date',
        'population',
        'total_area_mi_2',
        'total_area_km_2',
        'land_area_mi_2',
        'land_area_km_2',
        'water_area_mi_2',
        'water_area_km_2',
        'number_of_reps'
    ]
    rows = (line.strip().split('\t') for line in open(input_file, 'r'))
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        # Writer column headers.
        writer.writerow(headers)
        for row in rows:
            tokens = [t.strip() for t in row]
            # Replicate the third token for lines thatonly contain 12 tokens.
            if len(tokens) == 12:
                tokens = tokens[:3] + [tokens[2]] + tokens[3:]
            # Convert the ratification date to ISO format.
            tokens = tokens[:4] + [to_datetime(tokens[4]).isoformat()[:10]] + tokens[5:]
            # Remove ',' from numeric values.
            tokens = tokens[:5] + [t.replace(',', '') for t in tokens[5:]]
            writer.writerow(tokens)
