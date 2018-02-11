import csv 
import os

exec(open('getGeoLocation.py').read())
from pathlib import Path

CURRENT_PATH = os.getcwd()

CSV_DIR = 'csvs'
MARKDOWN_DIR = 'markdowns'

FILES = [
	'clean_dataset_iz_test'
]

for file in FILES:

	p = Path(CURRENT_PATH)
	csv_folder = p / '..' / CSV_DIR
	markdown_folder = p / '..' / MARKDOWN_DIR

	with open('{}/{}.csv'.format(csv_folder,file), "r") as f:
		writeFile = open('{}/{}.csv'.format(csv_folder,file+"_out.csv"), "w")
		writer = csv.writer(writeFile, delimiter=',')
		reader = csv.DictReader(f)
		for row in reader:
			#For each CSV row
			
			#Do stuff to get the lat/lon
			
			writer.writerow([row["Tracking Number"], 'Lovely Spam', 'Wonderful Spam'])
	writeFile.close()