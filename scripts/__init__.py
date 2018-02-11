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

	print("found that {} tracking numbers were already written".format(len(completedTracking)))
	found_already_written=0
	wrote_to_file=0
	with open('{}/{}.csv'.format(csv_folder,file), "r",newline="", encoding="utf-8") as f:
		lat_long_write_file = open('{}/{}.csv'.format(csv_folder,file+"_latlong_out"), "w")
		full_dataset_write_file = open('{}/{}.csv'.format(csv_folder,file+"_fulldata_out"), "w")
		lat_long_fieldnames=["Tracking Number","Lat","Lng"]
		reader = csv.DictReader(f)
		full_dataset_fieldnames = reader.fieldnames + ['LatNew', 'LngNew']
		lat_long_writer = csv.DictWriter(lat_long_write_file, delimiter=',', fieldnames=lat_long_fieldnames)
		full_dataset_writer = csv.DictWriter(full_dataset_write_file, delimiter=',', fieldnames=full_dataset_fieldnames)
		if(len(completedTracking)==0):
			lat_long_writer.writeheader()
			full_dataset_writer.writeheader()
		for row in reader:
			#For each CSV row
			if(row["Tracking Number"] in completedTracking):
				found_already_written+=1
				continue
			tracking_number, lat, lng = query_map_api(row)
			lat_long_writer.writerow({"Tracking Number":row["Tracking Number"], "Lat":lat, "Lng":lng})
			new_row = {k: v for (k, v) in row.items()}
			new_row["LatNew"] = lat
			new_row["LngNew"] = lng
			full_dataset_writer.writerow(new_row)
			wrote_to_file+=1
			print("wrote tracking number {}".format(wrote_to_file+found_already_written))
	full_dataset_write_file.close()
	lat_long_write_file.close()
	print("did not write {} tracking numbers because they were already written".format(found_already_written))
	print("wrote {} tracking numbers".format(wrote_to_file))