import requests
import csv
import os
import os.path
from collections import OrderedDict

from pathlib import Path

CURRENT_PATH = os.getcwd()

CSV_DIR = 'csvs'
MARKDOWN_DIR = 'markdowns'

FILES = [
    'clean_dataset_iz_test_out.csv'
]

url="http://hackthedeep.liweb.group/dirtydata/"

def upload(row):
    print(row)
    update={"clean_latitude":row["Lat"],"clean_longitude":row["Lng"]}
    r=requests.put(url+row["Tracking Number"], data=update)
    print(r.text)
    print("uploaded")

for file in FILES:

    p = Path(CURRENT_PATH)
    csv_folder = p / '..' / CSV_DIR
    markdown_folder = p / '..' / MARKDOWN_DIR
    completedTracking = []

    with open('{}/{}.csv'.format(csv_folder,file), "r",newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            upload(row)
