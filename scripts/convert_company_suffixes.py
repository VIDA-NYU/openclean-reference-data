# This file is part of the Data Cleaning Library (openclean).
#
# Copyright (C) 2018-2021 New York University.
#
# openclean is released under the Revised BSD License. See file LICENSE for
# full license details.

"""Helper functin to convert the list of company suffixes extracted using regex
from https://www.harborcompliance.com/information/company-suffixes
"""

import csv
import sys


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
    # Parse input file, create set of distinct values (case sensitive), and
    # write the result to a single column CSV file.
    headers = ['company_suffix']
    values = set(line.strip() for line in open(input_file, 'r'))
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        # Writer column headers.
        writer.writerow(headers)
        for val in values:
            writer.writerow([val])
