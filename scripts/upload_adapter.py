import requests
import csv
import os
import os.path
import time
from collections import OrderedDict

from pathlib import Path

CURRENT_PATH = os.getcwd()

CSV_DIR = 'csvs'
MARKDOWN_DIR = 'markdowns'

FILES = [
    'dirty_dataset_iz_latlong_out'
]

url="http://hackthedeep.liweb.group/dirtydata/"

def upload(row):
    print(row)
    update={"clean_latitude":row["Lat"],"clean_longitude":row["Lng"]}
    if( (row["Lat"] is not None and row["Lat"]!="") or (row["Lng"] is not None and ["Lng"]!="")):
        #Check to see if it's already there.
        r=requests.get(url+row["Tracking Number"])
        if(r.json()["CleanLatitude"] is not None and r.json()["CleanLatitude"]!=""):
            r=requests.put(url+row["Tracking Number"], data=update)
            print(r.text)
            print("uploaded")
            time.sleep(5)
        else:
            print("Did not update because already found")
    else:
        print("Did not update because nothing to update")

for file in FILES:

    p = Path(CURRENT_PATH)
    csv_folder = p / '..' / CSV_DIR
    markdown_folder = p / '..' / MARKDOWN_DIR
    completedTracking = []

    with open('{}/{}.csv'.format(csv_folder,file), "r",newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                upload(row)
            except:
                print("did not update")
                print(row)
