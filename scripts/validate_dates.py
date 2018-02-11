import csv
import os
from pathlib import Path
from dateutil import parser
import arrow

CURRENT_PATH = os.getcwd()

CSV_DIR = 'csvs'
MARKDOWN_DIR = 'markdowns'

FILES = [
    # 'herpetology_seasnakes',
    # 'ichthyology_marine_collections',
    # 'mammalogy_marine_mammals',
    # 'ornithology_specimens_aquatic_localities',
    'clean_dataset_iz',
    # 'dirty_dataset_iz'
]


for file in FILES:
    
    p = Path(CURRENT_PATH)
    csv_folder = p / '..' / CSV_DIR
    markdown_folder = p / '..' / MARKDOWN_DIR

    with open(f'{csv_folder}/{file}.csv') as f:
        reader = csv.DictReader(f)

        filled_counter = 0
        total_rows = 0
        failed_rows = []

        for index, row in enumerate(reader):
            if row['Date Rcvd verbatim'] != '':
                date = row['Date Rcvd verbatim']
                try:
                    dt = parser.parse(date)
                    filled_counter = index + 1
                except ValueError:
                    failed_rows.append({'Tracking Number':row['Tracking Number'], 'content_date': date})


            total_rows += 1

        with open(f'{csv_folder}/unformattable_dates.csv', 'w', newline='') as dates:
        
            fieldnames = ['Tracking Number', 'content_date']
            writer = csv.DictWriter(dates, fieldnames=fieldnames)

            writer.writeheader()
            
            writer.writerows(failed_rows)

        with open('date_datalog', 'w') as log:
            log.write(str(failed_rows))


    print(f'There are {filled_counter} filled in records')
    print(f'There are {len(failed_rows)} non parsable dates in the filled in records')
    print(f'Of a total of {total_rows}')
