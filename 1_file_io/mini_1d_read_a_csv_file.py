# Instructions: 
#    * You have been provided a CSV file "example_in.csv"
#      use a text editor to look at this file.
#    * Then open the file with a spreadsheet program such a 
#      Microsoft Excel or OSX numbers. You can see how this
#      is a simple 'exchange format'.
#    * Then write Python below to read the information from "example_in.csv"
#      and print out the data to the screen in a readable way.
#
# Hint: look at the second page from fileio_in_python.pdf reference card! 

import csv
with open("example_in.csv") as file_in:
    csv_reader = csv.reader(file_in)
    for row in csv_reader:
        print(row)
