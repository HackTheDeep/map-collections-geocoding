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
	
	if(os.path.isfile('{}/{}.csv'.format(csv_folder,file+"_out.csv"))):
		with open('{}/{}.csv'.format(csv_folder,file+"_out.csv"), "r") as f:
			reader = csv.DictReader(f)
			for row in reader:
				completedTracking.append(row["Tracking Number"])

	country_replace = {}
	with open('{}/{}.csv'.format(p / '..' / "Locations/dirty_locations","countries_offbyone_unique"), "r",encoding="utf-8") as f:
		reader = csv.reader(f,delimiter='\t')
		for from_country,to_country in reader:
			country_replace.update({from_country:to_country})


	print("found that {} tracking numbers were already written".format(len(completedTracking)))
	found_already_written=0
	wrote_to_file=0
	with open('{}/{}.csv'.format(csv_folder,file), "r",newline="", encoding="utf-8") as f:
		writeFile = open('{}/{}.csv'.format(csv_folder,file+"_out.csv"), "a")
		writeFieldnames=["Tracking Number","Lat","Lng"]
		writer = csv.DictWriter(writeFile, delimiter=',', fieldnames=writeFieldnames)
		if(len(completedTracking)==0):
			writer.writeheader()
			
		reader = csv.DictReader(f)
		for row in reader:
			#For each CSV row
			if(row["Tracking Number"] in completedTracking):
				found_already_written+=1
				continue

			#Replace country records
			if(row['Country'] in country_replace.keys()):
				row.update({'Country':country_replace[row['Country']]})
				print(row)
			tracking_number, lat, lng = query_map_api(row)
			
			writer.writerow({"Tracking Number":row["Tracking Number"], "Lat":lat, "Lng":lng})
			wrote_to_file+=1
			print("wrote tracking number {}".format(wrote_to_file+found_already_written))
	writeFile.close()
	print("did not write {} tracking numbers because they were already written".format(found_already_written))
	print("wrote {} tracking numbers".format(wrote_to_file))