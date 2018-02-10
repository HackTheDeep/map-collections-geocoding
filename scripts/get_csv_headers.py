import csv 

CSV_DIR = '../CSVS'
FILES = [
	'herpetology_seasnakes',
	'ichthyology_marine_collections',
	'mammalogy_marine_mammals',
	'ornithology_specimens_aquatic_localities',

]


for file in FILES:
	headers = [];

	with open(f'{file}.csv') as f:
		reader = csv.DictReader(f)
		print(reader)



