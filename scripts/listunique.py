#!/usr/bin/python

# Read dirty data csv files print lists of data from columns you're interested in
# In this case location related ones
#
# NOTE this is assuming UTF-8 encoded files

import StringIO
import unicodecsv as csv
import codecs
import sys

# variables
oceanCol = 105
continentCol = 104
countryCol = 115
stateCol = 116
countyCol = 117
cityCol = 118
localeCol = 119

oceanCsv = "oceans.csv"
continentCsv = "continents.csv"
countryCsv = "countries.csv"
stateCsv = "states.csv"
countyCsv = "counties.csv"
cityCsv = "cities.csv"
localeCsv = "locales.csv"

folder = "../Locations/dirty_locations/"
file1 = open(folder + oceanCsv, "w+")
file2 = open(folder + continentCsv, "w+")
file3 = open(folder + countryCsv, "w+")
file4 = open(folder + stateCsv, "w+")
file5 = open(folder + countyCsv, "w+")
file6 = open(folder + cityCsv, "w+")
file7 = open(folder + localeCsv, "w+")

input = "../csvs/dirty_dataset_iz_utf8.csv"

# big data sets need this
csv.field_size_limit(sys.maxsize)

# open the input file
f = codecs.open(input, encoding="utf-8")
reader = csv.reader(f, encoding="utf-8")
 
# skips header row
next(reader)

# loop through the data
for cols in reader:    
    if cols[oceanCol] != "":
        file1.write('%s\n' % cols[oceanCol])
    if cols[continentCol] != "":
        file2.write('%s\n' % cols[continentCol])
    if cols[countryCol] != "":
        file3.write('%s\n' % cols[countryCol])
    if cols[stateCol] != "":
        file4.write('%s\n' % cols[stateCol])
    if cols[countyCol] != "":
        file5.write('%s\n' % cols[countyCol])
    if cols[cityCol] != "":
        file6.write('%s\n' % cols[cityCol])
    if cols[localeCol] != "":
        file7.write('%s\n' % cols[localeCol])

#close the output files
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()

print "done"
