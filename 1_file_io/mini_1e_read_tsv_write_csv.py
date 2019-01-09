# Instructions: 
#
# write Python to read in the data from tsv file 
# 'lmb_nobel_prizes.tsv' then
# (a) in the Nobel Prize Winners items, replace the '&' characters with 'and'
# (b) print out each row to the secreen
# (c) save just the dates and names in a new CSV file 'lmb_out.csv'
#
# Question: in 2002 there are 3 prize winners and so there is a comma in the 
# names field how is this handled in the output CSV file?
#
# Hint: look at the second page from fileio_in_python.pdf reference card! 

import csv
with open('lmb_nobel_prizes.tsv') as tsv:
    reader = csv.reader(tsv, delimiter='\t')
    data = list(reader)

for row in data:
    row[1] = row[1].replace('&', 'and')
    print(row)

# TODO osmart Jan 2019: (c) save just the dates and names in a new CSV file 'lmb_out.csv'

