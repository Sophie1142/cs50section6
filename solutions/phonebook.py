import csv
import sys

# Write a program [phonebook.py](http://phonebook.py) that reads
# from a CSV file (provided as a command-line argument) using a DictReader and
# prints out the data on each person in the phone book.
# The file contains columns name and number, representing
# each person's name and phone number, respectively.

# As a next step, add some error checking to ensure that
# (1) the program is run with a command-line argument, and
# (2) the CSV file contains both a name column and a number column.

if len(sys.argv) != 2:
    sys.exit("Usage: python phonebook.py data.csv")

f = open(sys.argv[1])
reader = csv.DictReader(f)

fields = reader.fieldnames
if "name" not in fields or "number" not in fields:
    sys.exit("File must have name and number columns")

for row in reader:
    name = row["name"]
    number = row["number"]
    print(f"{name}'s phone number is {number}")

f.close()