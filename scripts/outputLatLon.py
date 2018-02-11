import csv 
import os
import os.path
from collections import OrderedDict

from gen_query_strings import query_map_api

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
	completedTracking = []
	
	#if(os.path.isfile('{}/{}.csv'.format(csv_folder,file+"_out.csv"))):
	#	with open('{}/{}.csv'.format(csv_folder,file+"_out.csv"), "r") as f:
	#		reader = csv.DictReader(f)
	#		for row in reader:
	#			completedTracking.append(row["Tracking Number"])

	with open('{}/{}.csv'.format(csv_folder,file), "r") as f:
		writeFile = open('{}/{}.csv'.format(csv_folder,file+"_out.csv"), "w")
		writeFieldnames=["Tracking Number","Lat","Lng"]
		writer = csv.DictWriter(writeFile, delimiter=',', fieldnames=writeFieldnames)
		reader = csv.DictReader(f)
		for row in reader:
			#For each CSV row
			tracking_number, lat, lng = query_map_api(row)
			
			
			
			writer.writerow({"Tracking Number":row["Tracking Number"], "Lat":lat, "Lng":lng})
	writeFile.close()