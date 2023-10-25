#!/usr/bin/env python3
import csv
import os
import sys

from csv2vcf import convert_to_vcard
from member import Member


def main() -> None:
    # Input file must be a csv file formatted in the style produced by Google Forms
    path_input = sys.argv[1]
    path_output = "clean.csv"

    if not path_input:
        print("usage: python3 converter.py <input csv file>")
        exit(1)

    if not os.path.isfile(path_input):
        print(f"File {path_input} does not exist")

    members: list[Member]
    with open(path_input, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # First row is for headers, therefore ignore it.
        members = [Member.parse_list(line) for line in reader]

    with open(path_output, 'w') as file:
        for member in members:
            file.write(str(member))

    convert_to_vcard(path_output, single_output=True, input_file_format={"name": 1, "tel": 2, "email": 3, "note": 4})


if __name__ == "__main__":
    main()
