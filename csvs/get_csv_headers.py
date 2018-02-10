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
		
		counter = 0
		for row in reader:
			while counter < 1:
				print(row.keys())
				counter += 1

				headers = ''.join([f'* {header}   ' for header in row.keys()])
				data = f"""# FILE 	{file} ## HEADERS {headers}
				"""

				with open(f'{file}.md', 'w+') as readme:
					readme.write(data)



