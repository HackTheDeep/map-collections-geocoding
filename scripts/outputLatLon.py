import csv 
import os

exec(open('getGeoLocation.py').read())
from pathlib import Path

CURRENT_PATH = os.getcwd()

CSV_DIR = 'csvs'
MARKDOWN_DIR = 'markdowns'

FILES = [
	'clean_dataset_iz'
]

