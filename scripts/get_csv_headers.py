import csv 
import os
from pathlib import Path

CURRENT_PATH = os.getcwd()

CSV_DIR = 'csvs'
MARKDOWN_DIR = 'markdowns'

FILES = [
	'herpetology_seasnakes',
	'ichthyology_marine_collections',
	'mammalogy_marine_mammals',
	'ornithology_specimens_aquatic_localities',
	'clean_dataset_iz',
	'dirty_dataset_iz'
]


for file in FILES:
	
	p = Path(CURRENT_PATH)
	csv_folder = p / '..' / CSV_DIR
	markdown_folder = p / '..' / MARKDOWN_DIR

	with open(f'{csv_folder}/{file}.csv') as f:
		reader = csv.DictReader(f)
		
		counter = 0
		for row in reader:
			while counter < 1:
				
				counter += 1

				headers = ''.join(['* {} \n   '.format(header) for header in row.keys()])
				data = f"""# FILE 	{file}
## HEADERS 
{headers}
"""

				with open(f'{markdown_folder}/{file}.md', 'w+') as readme:
					readme.write(data)



