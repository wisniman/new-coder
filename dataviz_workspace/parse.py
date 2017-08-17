"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""

import csv

MY_FILE = "./data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Build a data structure to return parsed_data
    parsed_data = []
    fields = csv_data.next()
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV file
    opened_file.close()

    return parsed_data


def main():
    # Call the parse function and give it the needed parameters
    new_data = parse(MY_FILE, ",")

    # Print the data
    print(new_data)


if __name__ == '__main__':
    main()
