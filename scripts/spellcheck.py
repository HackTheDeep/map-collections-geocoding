#!/usr/bin/python

# Read dirty location data and attempt to make corrections within 1 edit distance
#
# NOTE this is assuming UTF-8 encoded files

import StringIO
import unicodecsv as csv
import codecs
import sys

folder = "../Locations/dirty_locations/"
output = open(folder + "countries_misspelled.csv", "w+")
output_ob1 = open(folder + "countries_offbyone.csv", "w+")

with open('../Locations/dicts/countries_clean.csv') as f:
    WORDS = map(str.lower,f.read().splitlines())

def candidates(word): 
#    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    return (known([word]) or known(edits1(word)))

def known(words): 
    return set(w for w in words if w in WORDS)

def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# variables
folder = "../Locations/dirty_locations/"
file1 = folder + "countries.csv"

# big data sets need this
csv.field_size_limit(sys.maxsize)

# loop through the data
f = codecs.open(file1, encoding="utf-8")
for location in f:   
    location = location.strip('\n').lower()
    if location not in WORDS:
        cand = candidates(location)
        if len(cand) > 0:
            output_ob1.write('{}\t{}\n'.format(location,cand.pop()))
        output.write('{}\n'.format(location))

output.close()
output_ob1.close()
print "done"
