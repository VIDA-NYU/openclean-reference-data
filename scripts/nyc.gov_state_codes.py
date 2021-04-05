# This file is part of the Data Cleaning Library (openclean).
#
# Copyright (C) 2018-2021 New York University.
#
# openclean is released under the Revised BSD License. See file LICENSE for
# full license details.

"""List of valid state codes for license plates published by the NYC Department
of Fincnace: http://www.nyc.gov/html/dof/html/pdf/faq/stars_codes.pdf
"""

import csv
import sys


def capitalize(value):
    return ' '.join([t.capitalize() for t in value.split()])


if __name__ == '__main__':
    """Expects two input files for U.S. states and other states and one output
    file.
    """
    args = sys.argv[1:]
    if len(args) != 3:
        print('usage: <us-states-file> <other-states-file> <output-file>')
        sys.exit(-1)
    us_file, other_file, output_file = args
    us_states = [[line[:2], capitalize(line[2:].strip())] for line in open(us_file, 'r')]
    other_states = [[line[:2], line[2:].strip()] for line in open(other_file, 'r')]
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['code', 'name', 'type'])
        for row in us_states:
            writer.writerow(row + ['US'])
        for row in other_states:
            writer.writerow(row + ['Other'])
